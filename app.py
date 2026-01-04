from flask import Flask, request,jsonify ,redirect, url_for, render_template, session
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from groq import Groq
from sentence_transformers import SentenceTransformer, util
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os
from dotenv import load_dotenv
import json
import csv
# Load .env file
load_dotenv()

# Start Flask application with instance_ relative config=True
app = Flask(__name__, instance_relative_config=True)

app.secret_key = 'your-secret-key' 
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the uploads folder
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)

# Job model definition
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    description = db.Column(db.Text)
    company = db.Column(db.String(255))
    location = db.Column(db.String(255))
    salary = db.Column(db.String(255)) 
    required_skills = db.Column(db.Text) 

# Check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'jpg', 'jpeg', 'png'}

# Extract Text from CV
def extract_text_from_cv(path):
    print(f"DEBUG: Extracting text from CV: {path}") # Debug
    try:
        if path.lower().endswith(".pdf"):
            images = convert_from_path(path)
            text = "\n".join(pytesseract.image_to_string(img) for img in images)
            print(f"DEBUG: Text length extracted from PDF: {len(text)}") # Debug
            return text
        elif path.lower().endswith((".jpg", ".jpeg", ".png")):
            text = pytesseract.image_to_string(Image.open(path))
            print(f"DEBUG: Text length extracted from image: {len(text)}") # Debug
            return text
        else:
            print("DEBUG: Unsupported file format.") # Debug
            return ""
    except Exception as e:
        print(f"ERROR: Error while extracting text from CV: {e}") # Debug
        return ""

# Veritabanından iş tanımlarını al
def job_descriptions_from_db():
    jobs = Job.query.all()
    print(f"DEBUG: Number of job postings pulled from database: {len(jobs)}") # Debug
    return jobs

# Start the Groq API client
groq_api_key = os.environ.get("GROQ_API_KEY")
print(f"DEBUG: GROQ_API_KEY from environment: {'****' + groq_api_key[-4:] if groq_api_key else 'None/Empty'}") # Debug
client = Groq(api_key=groq_api_key)


# Load SentenceTransformer model
try:
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("DEBUG: SentenceTransformer model loaded successfully.") # Debug
except Exception as e:
    print(f"ERROR: Error loading Sentence Transformer model: {e}") # Debug
    model = None # Set to None if model cannot be loaded

@app.route('/', methods=['GET', 'POST'])
def upload_cv():
    if request.method == 'POST':
        print("DEBUG: POST request received.") # Debug
        if 'file' not in request.files:
            print("DEBUG: 'file' not found.") # Debug
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print("DEBUG: File name is empty.") # Debug
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(save_path)
            print(f"DEBUG: File saved: {save_path}") # Debug

            text = extract_text_from_cv(save_path)
            print(f"DEBUG: General text extracted from CV (pre-summary): {text[:200]}...") 
            if not text.strip():
                print("WARNING: Text could not be extracted from the CV or the text is empty.") # Debug
                return render_template('index.html', error_message="Could not extract text from CV. Please try another CV or check its content.")


            try:
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[{
                        "role": "user",
                        "content": (
                            "Generate a professional English job description for a role that *matches the qualifications and experience described in the CV below*. "
                            "The output should be formatted as a typical job posting, including sections like 'Job Summary', 'Experiences','Responsibilities', 'Requirements', and 'Skills'.\n\n"
                            "CV:\n\"\"\"{}\"\"\""  
                        ).format(text)
                    }]
                )
                summary = response.choices[0].message.content.strip()
                print("\n---CV Summary Start ---")
                print(summary)
                print("--- CV Summary End ---\n")
                if not summary.strip():
                    print("WARNING: Empty summary from Groq.") # Debug
                    return render_template('index.html', error_message="There was a problem summarizing your CV. Please check the CV content.")

            except Exception as e:
                print(f"ERROR: Error while calling Groq API: {e}") # Debug
                return render_template('index.html', error_message=f"An error occurred while summarizing the CV: {e}")

            if model: 
                cv_embed = model.encode(summary, convert_to_tensor=True)
                print("DEBUG: CV summary embedded.") # Debug
            else:
                print("ERROR: Matching failed because SentenceTransformer model could not be loaded.") # Debug
                return render_template('index.html', error_message="Matching service is unavailable.")

            matches = []
            jobs_from_db = job_descriptions_from_db() # Call Function
            if not jobs_from_db:
                print("WARNING: No job posting found in database!") # Debug
                return render_template('index.html', error_message="No job postings were found in the database to match. Please check the database.")


            for job in jobs_from_db:
                job_embed = model.encode(job.description, convert_to_tensor=True)
                score = util.pytorch_cos_sim(cv_embed, job_embed).item()
                matches.append({
                    "title": job.title,
                    "description": job.description,
                    "score": score * 100,  
                    "company": job.company,  
                    "location": job.location,  
                    "salary": job.salary,  
                    "required_skills": job.required_skills  
                })


            matches = sorted(matches, key=lambda x: -x['score'])[:5]
            THRESHOLD_SCORE = 50
           # Check if only the HIGHEST scoring listing has passed the threshold
            if matches and matches[0]['score'] < THRESHOLD_SCORE:
                # If even the highest scoring ad is below the threshold, show no results
                final_matches = []
                session['message'] = "Sorry, there were no suitable or sufficient job postings matching your CV."
                print(f"DEBUG: En yüksek skor ({matches[0]['score']:.2f}%) eşiğin ({THRESHOLD_SCORE}%) altında. Hiçbir ilan gösterilmeyecek.")
            else:
                final_matches = matches[:5] # Sadece ilk 5 eşleşmeyi al
                session.pop('message', None) # Eğer önceden bir mesaj varsa temizle
                print(f"DEBUG: En yüksek skor ({matches[0]['score']:.2f}%) eşiğin ({THRESHOLD_SCORE}%) üzerinde. Eşleşen ilanlar gösterilecek.")


            print(f"DEBUG: Eşleşen iş ilanları (nihai liste): {final_matches}") # Debug

            # Store only necessary, small information in the session.
            session['matches'] = [
                {
                    "title": job.get("title"),
                    "score": job.get("score"),
                    "company": job.get("company"),
                    "location": job.get("location"),
                    "required_skills": job.get("required_skills")
                }
                for job in final_matches
            ]
            return redirect(url_for('show_results'))
    return render_template('index.html')

@app.route('/reset')
def reset_session():
    session.pop('matches', None)  # clear matches information
    return redirect(url_for('upload_cv'))  # Redirect to home page (CV upload)

@app.route('/results')
def show_results():
    matches = session.get('matches')
    if not matches:
        print("DEBUG: Session'da eşleşme bulunamadı, kullanıcıya mesaj gösteriliyor.") # Debug
        # results.html'e boş bir 'matches' listesi ve bir 'error_message' gönder
        return render_template('results.html', matches=[], error_message="Üzgünüz, CV'nizle eşleşen iş ilanı bulunamadı. Lütfen başka bir CV deneyin.")
    print(f"DEBUG: results.html'e gönderilen eşleşmeler: {matches}") # Debug
    return render_template('results.html', matches=matches)


if __name__ == '__main__':
    app.run(debug=True)


