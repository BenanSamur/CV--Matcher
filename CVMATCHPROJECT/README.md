# CV-Job Matching Project

This project is a web application that matches user-uploaded CVs with job postings using AI techniques.

---

## Requirements

- Python 3.8 or higher  
- Python packages listed in `requirements.txt`

---

## Setup

1. Download or extract the project folder to your computer.

2. (Optional but recommended) Create a virtual environment:

   python -m venv venv

3. Activate the virtual environment:

   - On Windows:  
     .\venv\Scripts\activate

   - On Linux/Mac:  
     source venv/bin/activate

4. Install the required packages:

   pip install -r requirements.txt

5. Create a .env file in the root directory of the project. Add the following environment variables:

   -Hugging Face API Key:
    HF_TOKEN= your-huggingface-api-key

   -Groq API Key:
    GROQ_API_KEY= your-groq-api-key
---

## Running the Project

Start the application by running the following command in the terminal:

   python app.py

The app will run by default at `http://127.0.0.1:5000`. Open this address in your browser to use it.

---

## Notes

- Large or sensitive files such as `my_model/`, `venv/`, and `.env` are excluded from the submitted archive.  
- Necessary models and data should be obtained separately.

