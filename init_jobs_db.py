from app import app, db, Job

with app.app_context():
    db.create_all()

    # Sadece veritabanı boşsa iş ilanlarını ekle
    if Job.query.first() is None:
        jobs = [
            Job(
                title="Civil Engineer – Infrastructure Projects",
                description="""
We are seeking a Civil Engineer to oversee road and bridge construction projects. Responsibilities include structural analysis, material selection, and site supervision.

Qualifications:
- Bachelor's degree in Civil Engineering
- Proficiency in AutoCAD, SAP2000, and STAAD.Pro
- Experience with infrastructure or transportation projects
- Strong knowledge of construction materials and project management
- Ability to work on-site and manage contractors

Responsibilities:
Perform structural analysis and design for road and bridge projects.
Select appropriate construction materials, ensuring compliance with quality and safety standards.
Supervise on-site construction activities, monitoring progress and adherence to plans.
Collaborate with project stakeholders, including contractors and regulatory bodies.
Prepare technical reports, project documentation, and progress updates.
""",
                company="ConstructCo",
                location="Istanbul, Turkey",
                salary="₺80,000 - ₺120,000 per month",
                required_skills="AutoCAD, SAP2000, STAAD.Pro, Project Management, Construction Materials"
            ),

            Job(
                title="Electrical Engineer – Power Systems",
                description="""
Hiring an Electrical Engineer to design and maintain medium and high-voltage power systems for industrial facilities.

Qualifications:
- BSc in Electrical or Electronics Engineering
- Familiarity with power system analysis software (ETAP, PSS/E)
- Knowledge of circuit design, transformers, and switchgear
- Hands-on experience with power distribution and safety standards
- Strong technical documentation and teamwork skills

Responsibilities:
Design and develop medium and high-voltage power systems for industrial applications.
Conduct power system analysis using software like ETAP and PSS/E.
Oversee the installation, testing, and maintenance of electrical equipment, including transformers and switchgear.
Ensure all designs and installations comply with relevant electrical safety standards and regulations.
Prepare detailed technical specifications, schematics, and project reports.
""",
                company="ElectroPower Inc.",
                location="Ankara, Turkey",
                salary="₺75,000 - ₺110,000 per month",
                required_skills="ETAP, PSS/E, Circuit Design, Transformers, Switchgear, Power Distribution"
            ),
            Job(
                title="Landscape Architecture Assistant – Entry-Level Position",
                description="""
We are looking for a passionate and environmentally conscious Landscape Architecture Assistant to join our growing team. This role is ideal for recent graduates eager to apply their academic knowledge to real-world projects and contribute to sustainable and aesthetically pleasing outdoor designs.

Qualifications:
- Bachelor's degree in Landscape Architecture or a related field (recent graduate or final-year student)
- Basic proficiency in AutoCAD, SketchUp, and V-Ray for landscape modeling and technical drawing
- Knowledge of plant species and landscape materials
- Experience in site observation and landscape planning is a plus
- Familiarity with Adobe Creative Suite (especially Photoshop) and ArcGIS is an advantage
- Strong communication and teamwork skills
- Detail-oriented and eager to contribute to sustainable design practices
- Intermediate English proficiency

Responsibilities:
Assist in the preparation of technical drawings and landscape design layouts
Support site survey processes and help compile plant and material lists
Create basic 3D models and rendering visuals for client presentations
Contribute to general in-office tasks including document preparation and project coordination
Participate in creative discussions and contribute design ideas
""",
                company="GreenScape Landscape Architecture",
                location="Istanbul, Turkey",
                salary="₺35,000 - ₺50,000 per month (based on experience)",
                required_skills="Landscape Design, AutoCAD, SketchUp, V-Ray, Plant Knowledge, Site Observation, Teamwork, Photoshop"
            ),
          Job(
                title="R&D Engineer – Innovative Product & Process Development",
                description="""
We are looking for a proactive and detail-oriented R&D Engineer to join our innovation team. The successful candidate will work on cutting-edge research and development projects, supporting the creation and optimization of new products and processes. This role is open to graduates from various engineering backgrounds such as Chemical, Mechanical, Materials, or Industrial Engineering.

Qualifications:
- Bachelor's degree in Engineering (Chemical, Mechanical, Materials, Industrial, or similar)
- 1–4 years of experience in R&D or innovation projects (preferred)
- Familiarity with lab work, product testing, or industrial process analysis
- Strong skills in data evaluation, reporting, and experiment design
- Proficiency in MS Office and preferably technical drawing/simulation tools
- Analytical thinking, strong communication skills, and team spirit
- Fluency in English

Responsibilities:
- Research, develop, and improve new products and manufacturing processes
- Conduct literature and patent reviews to support innovation strategies
- Design experiments, analyze data, and derive technical insights
- Prepare project documentation and technical reports
- Collaborate with cross-functional teams including production, QA, and design

""",
                company="InnoTek R&D and Engineering Inc.",
                location="Ankara, Turkey",
                salary="₺50,000 - ₺75,000 per month",
                required_skills="R&D, Project Management, Experiment Design, Technical Reporting, Problem Solving, MS Office, Team Collaboration"
            ),


            Job(
                title="Data Analyst – Business Intelligence",
                description="""
Seeking a Data Analyst to support strategic decision-making by analyzing business data and creating dashboards.

Qualifications:
- Bachelor’s degree in Statistics, Economics, or a related field
- Proficient in SQL, Excel, and data visualization tools (Tableau/Power BI)
- Understanding of statistical methods and business KPIs
- Ability to clean, process, and interpret large datasets
- Strong critical thinking and data storytelling skills

Responsibilities:
Collect, clean, and process large and complex datasets from various sources.
Conduct in-depth statistical analysis to identify trends, patterns, and insights.
Develop and maintain interactive dashboards and reports using Tableau or Power BI to visualize key performance indicators (KPIs).
Provide actionable insights and recommendations to support strategic business decisions.
Collaborate with cross-functional teams to understand data requirements and deliver impactful analytical solutions.

""",
                company="Data Insights Co.",
                location="Istanbul, Turkey",
                salary="₺60,000 - ₺90,000 per month",
                required_skills="SQL, Excel, Tableau, Power BI, Statistical Methods, Data Cleaning"
            ),

            Job(
                title="Art Director – Creative Branding",
                description="""
We are hiring an Art Director to lead visual branding and marketing campaigns for global clients.

Qualifications:
- Degree in Graphic Design, Visual Communication, or similar
- Proficiency in Adobe Creative Suite (Photoshop, Illustrator, InDesign)
- Experience in managing design teams and creative processes
- Strong portfolio in branding, packaging, or advertising
- Understanding of digital and print design best practices

Responsibilities:
Lead the conceptualization and execution of visual branding and marketing campaigns.
Direct and manage a team of designers, providing creative guidance and feedback.
Oversee the development of creative assets for both digital and print platforms, ensuring brand consistency.
Present creative concepts and strategies to clients, incorporating feedback effectively.
Stay updated on design trends and industry best practices to ensure innovative and effective solutions.
""",
                company="Creative Minds Agency",
                location="Izmir, Turkey",
                salary="₺65,000 - ₺95,000 per month",
                required_skills="Adobe Creative Suite, Graphic Design, Branding, Marketing Campaigns"
            ),

            Job(
                title="Mechanical Engineer – R&D and Prototyping",
                description="""
We are looking for a Mechanical Engineer to join our R&D team and develop prototypes for new consumer products.

Qualifications:
- BSc in Mechanical Engineering
- Skilled in CAD tools (SolidWorks, CATIA)
- Knowledge of thermodynamics, material science, and mechanics
- Hands-on experience with 3D printing and prototyping tools
- Team player with a passion for innovation

Responsibilities:
Design and develop mechanical components and systems for new consumer products using CAD software.
Apply principles of thermodynamics, material science, and mechanics in product development.
Create and test prototypes using 3D printing and other rapid prototyping tools.
Conduct experiments and simulations to validate designs and optimize product performance.
Collaborate with cross-functional R&D teams to bring innovative product concepts to fruition.
""",
                company="InnovateTech",
                location="Bursa, Turkey",
                salary="₺70,000 - ₺100,000 per month",
                required_skills="SolidWorks, CATIA, Thermodynamics, 3D Printing, Prototyping"
            ),

            Job(
                title="Computer Engineer – Embedded Systems",
                description="""
Join our team as a Computer Engineer to develop firmware and embedded systems for IoT products.

Qualifications:
- Bachelor’s degree in Computer Engineering or related
- Proficient in C/C++ and RTOS-based development
- Familiarity with microcontrollers (STM32, ESP32) and communication protocols (SPI, I2C, UART)
- Ability to read schematics and work with hardware teams
- Strong problem-solving and debugging skills

Responsibilities:
Design, develop, and test firmware for embedded systems in IoT products.
Work with various microcontrollers (e.g., STM32, ESP32) and implement RTOS-based solutions.
Integrate and debug communication protocols such as SPI, I2C, and UART.
Collaborate closely with hardware engineers to ensure seamless software-hardware interaction.
Troubleshoot and resolve complex issues in embedded systems, from design to deployment.
""",
                company="IoT Solutions Ltd.",
                location="Istanbul, Turkey",
                salary="₺85,000 - ₺130,000 per month",
                required_skills="C/C++, RTOS, Microcontrollers, SPI, I2C, UART, Hardware Debugging"
            ),

            Job(
                title="Social Media Manager – Brand Engagement",
                description="""
Looking for a Social Media Manager to boost engagement and grow our online presence.

Qualifications:
- Experience with Instagram, Twitter, LinkedIn, TikTok
- Content planning and influencer collaboration skills
- Knowledge of analytics tools (Meta, Hootsuite)
- Creativity and copywriting ability

Responsibilities:
Develop and implement comprehensive social media strategies to increase brand engagement and reach.
Plan, create, and schedule engaging content across various platforms, including Instagram, Twitter, LinkedIn, and TikTok.
Identify and collaborate with influencers to expand brand visibility and impact.
Monitor social media performance using analytics tools (e.g., Meta Business Suite, Hootsuite) and generate regular reports.
Write compelling and creative copy for social media posts, ads, and campaigns.
""",
                company="EngageLab",
                location="Istanbul, Turkey",
                salary="₺55,000 - ₺85,000 per month",
                required_skills="Social Media, Content Strategy, Analytics, Copywriting"
            ),

            Job(
                title="Senior Human Resources Specialist",
                description="""
Lead and manage end-to-end HR operations including talent acquisition, performance management, and employee engagement initiatives in a dynamic corporate environment.

Qualifications:

- Bachelor's degree in Human Resources, Business Administration, or a related field
- 5+ years of experience in comprehensive HR roles, especially in recruitment and performance development
- Proven success in implementing HR digitalization and satisfaction survey systems
- Proficiency in SAP HR or Workday and strong command of MS Office tools
- Excellent interpersonal and communication skills
- Fluent in English and native in Turkish

Responsibilities:
Oversee the full talent acquisition lifecycle, from sourcing and interviewing to onboarding.
Develop and manage performance management systems, including goal setting, reviews, and feedback processes.
Design and implement employee engagement initiatives to foster a positive and productive work environment.
Drive HR digitalization efforts, including the adoption of new HR software and processes.
Utilize HRIS systems like SAP HR or Workday for efficient data management and reporting.
Provide expert guidance on HR policies, procedures, and best practices to employees and management.
""", 
                company="FutureWork Technologies", 
                location="Istanbul, Turkey (Hybrid)", 
                salary="₺80,000 - ₺120,000 per month", 
                required_skills="Talent Acquisition, Performance Management, HR Digitalization, SAP HR, Employee Engagement, Interviewing Techniques"                 
            ),

            Job(
                title="Marketing Specialist – Digital Campaigns",
                description="""
We are hiring a Marketing Specialist to plan and execute digital marketing campaigns across various channels.

Qualifications:
- Degree in Marketing, Communication, or related
- Experience with SEO, SEM, Google Ads, and social media marketing
- Strong copywriting and content creation skills
- Ability to analyze campaign performance using tools like Google Analytics
- Creativity and attention to detail

Responsibilities:
Plan, execute, and optimize digital marketing campaigns across multiple channels, including SEO, SEM, social media, and Google Ads.
Conduct keyword research and optimize website content for search engine visibility.
Create compelling ad copy and visual content for digital campaigns.
Monitor and analyze campaign performance using tools like Google Analytics, providing regular reports and actionable insights.
Stay up-to-date with the latest digital marketing trends and technologies to ensure campaign effectiveness.
""",
                company="Digital Growth Agency",
                location="Ankara, Turkey",
                salary="₺55,000 - ₺80,000 per month",
                required_skills="SEO, SEM, Google Ads, Social Media Marketing, Copywriting, Google Analytics"
            ),

            Job(
                title="Architect – Sustainable Design",
                description="""
Looking for an Architect to design eco-friendly and modern living spaces with an emphasis on sustainability.

Qualifications:
- Bachelor's or Master’s degree in Architecture
- Experience with Revit, AutoCAD, and sustainable design tools
- Knowledge of LEED or BREEAM certification standards
- Ability to work on concept design and detailed drawings
- Strong aesthetic sense and team collaboration skills

Responsibilities:
Develop innovative and sustainable architectural designs for residential and commercial projects.
Utilize software like Revit and AutoCAD for creating detailed drawings and models.
Incorporate sustainable design principles and work towards LEED or BREEAM certification standards.
Manage projects from concept development through to construction documentation.
Collaborate with clients, engineers, and construction teams to ensure project success and client satisfaction.
""",
                company="GreenBuild Architects",
                location="Izmir, Turkey",
                salary="₺70,000 - ₺105,000 per month",
                required_skills="Revit, AutoCAD, Sustainable Design, LEED, BREEAM"
            ),
            Job(
                title="Sales Representative",
                description="""
We are seeking a highly motivated and target-oriented Sales Representative to join our dynamic team. The ideal candidate will have a proven track record in new customer acquisition, client relationship management, and consistently exceeding sales targets, preferably within a technology company. This role requires strong negotiation and persuasion skills to effectively present complex products and services to potential clients.

Key Responsibilities:

- Consistently meet and exceed monthly, quarterly, and annual sales targets.
- Identify and develop new business opportunities through various channels, including cold calling, email marketing, and LinkedIn.
- Build and maintain strong, long-lasting client relationships.
- Understand client needs and provide tailored software solutions through compelling presentations.
- Effectively utilize Customer Relationship Management (CRM) software to manage sales pipelines and enhance customer satisfaction and loyalty.
- Stay updated on industry trends, competitor activities, and product knowledge.
- Prepare and present sales reports and forecasts.

Qualifications:

- Associate Degree in Marketing and Sales Management or a related field.
- Minimum of 2 years of experience as a Sales Representative, ideally in a technology company.
- Proven success in achieving and exceeding sales quotas.
- Strong proficiency in Sales & Business Development.
- Hands-on experience with Customer Relationship Management (CRM) software (e.g., Salesforce).
- Excellent presentation, negotiation, and persuasion skills.
- Ability to conduct cold calling and lead generation effectively.
- Proficient in MS Office applications.
- Exceptional communication and interpersonal skills.
- Target-driven, self-motivated, and able to work independently as well as part of a team.
""",
                company="Innovative Tech Solutions",
                location="Istanbul, Turkey (Hybrid)",
                salary="₺45,000 - ₺65,000 per month",
                required_skills="Sales & Business Development, Customer Relationship Management (CRM), Presentation Skills, Cold Calling & Lead Generation, Salesforce, Communication Skills, Negotiation, Persuasion"
            ),
            Job(
                title="Financial Analyst – Investment Strategy",
                description="""
We are seeking a Financial Analyst to evaluate investment opportunities and assist with budgeting and forecasting.

Qualifications:
- Bachelor’s in Finance, Economics, or related discipline
- Proficiency in Excel, financial modeling, and data analysis
- Familiar with tools like Bloomberg Terminal or Morningstar
- Ability to interpret financial statements and assess risk
- Excellent reporting and communication abilities

Responsibilities:
Conduct in-depth financial analysis to evaluate potential investment opportunities.
Develop and maintain complex financial models for budgeting, forecasting, and valuation.
Utilize financial data tools such as Bloomberg Terminal or Morningstar for research and insights.
Interpret financial statements and perform comprehensive risk assessments for various assets.
Prepare clear and concise financial reports and presentations for stakeholders and management.
""",
                company="Capital Advisors",
                location="Istanbul, Turkey",
                salary="₺65,000 - ₺95,000 per month",
                required_skills="Excel, Financial Modeling, Data Analysis, Bloomberg Terminal, Risk Assessment"
            ),
            Job(
                title="Sales Representative-",
                description="""
We are seeking a highly motivated and target-driven Sales Representative to join our fast-growing team. The ideal candidate will have a solid track record in customer acquisition, account management, and consistently achieving sales targets, preferably within the software or technology sector. This role requires excellent communication skills and the ability to present complex solutions clearly to diverse clients.

Key Responsibilities:

- Achieve and exceed monthly and quarterly sales targets.
- Identify potential clients through cold calling, networking, and digital outreach.
- Develop and maintain strong relationships with customers to ensure repeat business.
- Conduct product demonstrations and tailor presentations to client needs.
- Manage sales pipelines effectively using CRM software.
- Keep abreast of industry trends, competitor offerings, and product updates.
- Prepare accurate sales reports and forecasts for management.

Qualifications:

- Associate Degree or Bachelor’s Degree in Marketing, Business, or related field.
- Minimum of 2 years of experience in sales, preferably in tech or software sales.
- Proven success in meeting or exceeding sales quotas.
- Proficiency with CRM tools such as Salesforce or Microsoft Dynamics.
- Strong negotiation and presentation skills.
- Comfortable with cold calling and lead generation.
- Excellent interpersonal and communication skills.
- Self-motivated and goal-oriented with the ability to work independently and as part of a team.
""",
                company="Innovative Tech Solutions",
                location="Istanbul, Turkey (Hybrid)",
                salary="₺47,000 - ₺67,000 per month",
                required_skills="Sales & Business Development, CRM (Salesforce, Microsoft Dynamics), Presentation Skills, Cold Calling, Lead Generation, Negotiation, Communication"
            ),


            Job(
                title="Customer Experience Manager – Telecommunications Sector",
                description="""
We are seeking a customer-centric and experienced Customer Experience Manager to lead our support operations and customer satisfaction strategies in the telecommunications sector. The ideal candidate will bring hands-on experience in CRM systems, complaint management, and customer loyalty programs.

Qualifications:
- Bachelor's degree in Public Relations, Communication, or a related field
- Minimum of 3 years of experience in customer relations or customer support roles
- Expertise in managing high-volume customer inquiries across multiple channels (phone, email, chat)
- Proficiency in CRM platforms, particularly Salesforce Service Cloud
- Strong communication skills (both written and verbal)
- Demonstrated ability to analyze customer feedback and implement effective service improvements
- Experience with stress management and problem-solving in fast-paced environments
- Familiarity with MS Office and reporting tools
- Empathy, customer focus, and collaborative mindset

Responsibilities:
- Oversee daily customer service operations and ensure high service quality
- Lead initiatives to improve customer satisfaction and retention
- Analyze customer feedback and implement data-driven improvements
- Coordinate across departments to resolve complex customer issues
- Monitor KPIs and provide regular reports on customer experience metrics
- Coach and mentor team members to build a high-performing support team
""",
                company="GlobalConnect Telecom",
                location="Ankara, Turkey",
                salary="₺50,000 - ₺70,000 per month (commensurate with experience)",
                required_skills="Customer Service, CRM (Salesforce), Complaint Resolution, Communication, MS Office, Customer Experience"
            ),
            Job(
                title="Chemical Process Engineer – Sustainable Industrial Solutions",
                description="""
We are seeking a talented and driven Chemical Process Engineer to join our R&D and production team, focusing on sustainable and innovative solutions in industrial chemical processes. The ideal candidate will possess strong analytical skills, hands-on experience with process optimization, and a passion for green technologies.

Qualifications:
- Bachelor’s or Master’s degree in Chemical Engineering
- 2-5 years of experience in chemical process development or production environments
- Knowledge of thermodynamics, mass transfer, and chemical reaction engineering
- Experience with Aspen Plus, MATLAB, or similar simulation tools
- Familiarity with sustainability metrics and life-cycle assessment is a plus
- Strong documentation and reporting skills
- Proficient in English and Turkish

Responsibilities:
- Design, simulate, and optimize chemical processes for production scale
- Collaborate with R&D and QA teams to ensure process safety and efficiency
- Monitor and analyze data from pilot and full-scale production units
- Support the implementation of eco-friendly and cost-effective process improvements
- Prepare technical documentation and participate in HAZOP studies
- Coordinate with suppliers, contractors, and regulatory bodies

""",
                company="EcoChem Industries",
                location="Izmir, Turkey",
                salary="₺55,000 - ₺80,000 per month",
                required_skills="Chemical Engineering, Aspen Plus, Process Optimization, MATLAB, Sustainability, HAZOP, Data Analysis"
            ),

            Job(
                title="Senior Digital Marketing Strategist – E-Commerce and Performance Marketing",
                description="""
We are looking for a data-driven and creative Senior Digital Marketing Strategist to join our fast-growing e-commerce marketing team. The ideal candidate will have solid experience in SEO, SEM, content marketing, and data analysis with a focus on driving performance and ROI.

Qualifications:
- Bachelor's degree in Marketing, Communication, or a related field
- At least 4 years of professional experience in digital marketing
- Proven track record in SEO, SEM, and social media marketing
- Proficient in Google Ads, Google Analytics, and Meta Business Suite
- Strong expertise in content strategy and conversion optimization
- Excellent skills in analyzing marketing metrics and campaign performance
- Hands-on experience with email marketing and A/B testing
- Fluent in English, with strong writing and reporting capabilities

Responsibilities:
- Design and execute comprehensive digital marketing strategies
- Manage and optimize paid ad campaigns (Google Ads, Facebook/Instagram)
- Monitor analytics dashboards and deliver insights to improve ROAS
- Develop SEO strategies to boost keyword rankings and organic visibility
- Collaborate with content teams to develop engaging marketing materials
- Track conversion metrics and continuously optimize the customer journey
""",
            company="BrightSphere Media Group",
            location="Remote / Istanbul, Turkey",
            salary="₺80,000 - ₺110,000 per month (based on experience)",
            required_skills="SEO, SEM, Google Ads, Google Analytics, Content Strategy, Meta Business Suite, Conversion Optimization, Data Analysis"
            ),

            Job(
                title="Software Engineer – Backend Development",
                description="""
We are seeking a Software Engineer to design, develop, and maintain scalable backend systems.

Qualifications:
- Bachelor’s in Computer Engineering, Software Engineering, or related field
- Strong knowledge of C#, Java, or Python
- Experience with RESTful APIs and database design (SQL/NoSQL)
- Familiarity with cloud services (AWS, Azure, GCP)
- Excellent problem-solving and teamwork skills

Responsibilities:
Design, develop, and implement robust and scalable backend services and APIs using C#, Java, or Python.
Work on database design and optimization, ensuring efficient data storage and retrieval using SQL or NoSQL databases.
Integrate and manage cloud services (AWS, Azure, GCP) to support application deployment and scalability.
Collaborate with frontend developers and other teams to ensure seamless system integration and functionality.
Debug, troubleshoot, and optimize existing backend systems to improve performance and reliability.

""",
                company="Tech Solutions Inc.",
                location="Ankara, Turkey",
                salary="₺90,000 - ₺140,000 per month",
                required_skills="C#, Java, Python, RESTful APIs, SQL, NoSQL, AWS, Azure, GCP"
            ),
            Job(
                title="Process Improvement Engineer",
                description="""
Drive efficiency and cost-saving initiatives across manufacturing operations through Lean methodologies, data analysis, and continuous improvement projects.

Qualifications:

- Bachelor’s degree in Industrial Engineering or related field
- 3+ years of experience in process improvement or manufacturing engineering roles
- Proven track record of applying Lean Manufacturing, Six Sigma, and Kaizen principles
- Hands-on experience with SAP and data analytics tools such as Minitab
- Strong skills in production planning, capacity analysis, and quality improvement
- Fluent in English and Turkish

Responsibilities:
Lead and facilitate continuous improvement projects using Lean Manufacturing, Six Sigma, and Kaizen methodologies to optimize production processes.
Conduct in-depth data analysis using tools like Minitab to identify inefficiencies, bottlenecks, and areas for cost reduction.
Develop and implement strategies for production planning, capacity utilization, and quality control.
Collaborate with various departments to ensure successful implementation of process improvements and adherence to new standards.
Prepare detailed reports on project progress, cost savings, and efficiency gain


""", 
                company="InnoTech Manufacturing Solutions", 
                location="Kocaeli, Turkey", 
                salary="₺65,000 - ₺95,000 per month", 
                required_skills="Lean Manufacturing, Six Sigma, Process Optimization, SAP, Data Analysis, Production Planning, Quality Control"
            ),

            Job(
                title="Data Scientist – Predictive Analytics",
                description="""
We are looking for a Data Scientist to build and deploy machine learning models for business insights.

Qualifications:
- Bachelor’s or Master’s in Computer Engineering, Data Science, or related field
- Experience with Python (pandas, scikit-learn, numpy)
- Knowledge of statistical modeling and time series analysis
- Familiarity with data visualization tools (Tableau, Power BI)
- Strong analytical and communication skills

Responsibilities:
Design, develop, and deploy machine learning models to solve complex business problems, with a focus on predictive analytics.
Utilize Python libraries like pandas, scikit-learn, and numpy for data manipulation, analysis, and model building.
Perform statistical modeling and time series analysis to identify trends and forecast future outcomes.
Create insightful data visualizations and dashboards using Tableau or Power BI to communicate findings to stakeholders.
Collaborate with business teams to understand requirements and translate them into data-driven solutions.
""",
                company="Predictive AI Labs",
                location="Istanbul, Turkey",
                salary="₺95,000 - ₺150,000 per month",
                required_skills="Python, Pandas, Scikit-learn, NumPy, Statistical Modeling, Tableau, Power BI"
            ),

            Job(
                title="Finance Analyst – Corporate Budgeting",
                description="""
Looking for a Finance Analyst to support annual budgeting, forecasting, and financial modeling.

Qualifications:
- Bachelor’s in Finance, Accounting, or Economics
- Strong Excel and financial modeling skills
- Experience with SAP or Oracle Financials
- Analytical mindset and presentation skills

Responsibilities:
Support the annual budgeting process, working with various departments to gather financial data and develop comprehensive budgets.
Prepare accurate financial forecasts and variance analysis to track performance against budget.
Develop and maintain complex financial models to support strategic decision-making and business planning.
Utilize financial systems such as SAP or Oracle Financials for data extraction and reporting.
Present financial reports and analysis to management, providing clear insights and recommendations.
""",
                company="FinScope Ltd.",
                location="Istanbul, Turkey",
                salary="₺75,000 - ₺110,000 per month",
                required_skills="Excel, SAP, Budgeting, Forecasting, Financial Modeling"
            ),

            Job(
                title="Cybersecurity Analyst – Threat Detection",
                description="""
We are hiring a Cybersecurity Analyst to monitor systems and respond to security threats.

Qualifications:
- Bachelor’s in Computer Engineering, Cybersecurity, or IT
- Understanding of firewalls, intrusion detection systems, and endpoint protection
- Experience with SIEM tools (Splunk, QRadar)
- Knowledge of network protocols and security best practices
- Strong attention to detail and incident response capabilities

Responsibilities:
Monitor security systems and tools, including firewalls, intrusion detection systems (IDS), and endpoint protection platforms, for suspicious activity.
Analyze security incidents and alerts using SIEM tools such as Splunk or QRadar.
Respond to security incidents, performing initial investigations and coordinating with relevant teams for resolution.
Stay informed about the latest cybersecurity threats, vulnerabilities, and security best practices.
Contribute to the development and improvement of security policies and procedures.
""",
                company="SecureNet Systems",
                location="Izmir, Turkey",
                salary="₺80,000 - ₺125,000 per month",
                required_skills="Firewalls, IDS, Endpoint Protection, SIEM, Splunk, QRadar, Network Protocols"
            ),
            
            Job(
                title="Embedded Systems Engineer – IoT Solutions",
                description="""
Join our team as an Embedded Systems Engineer developing firmware for IoT devices.

Qualifications:
- Degree in Computer Engineering, Electronics, or similar
- Proficiency in C/C++ and RTOS concepts
- Experience with microcontrollers (ARM, PIC) and hardware debugging tools
- Understanding of wireless protocols (Bluetooth, ZigBee, LoRa)
- Ability to work closely with hardware and software teams

Responsibilities:
Design, develop, and test embedded firmware for a range of IoT devices using C/C++.
Implement and optimize real-time operating systems (RTOS) for efficient device performance.
Work with various microcontrollers (e.g., ARM, PIC) and utilize hardware debugging tools to resolve issues.
Integrate and test wireless communication protocols such as Bluetooth, ZigBee, and LoRa.
Collaborate closely with hardware engineers to ensure seamless integration between hardware and firmware.
""",
                company="SmartThings Co.",
                location="Bursa, Turkey",
                salary="₺85,000 - ₺135,000 per month",
                required_skills="C/C++, RTOS, Microcontrollers, ARM, PIC, Bluetooth, ZigBee, LoRa"
            ),

            Job(
                title="AI Engineer – Natural Language Processing",
                description="""
We are seeking an AI Engineer to develop NLP applications for intelligent systems.

Qualifications:
- Bachelor’s or Master’s in Computer Engineering or Artificial Intelligence
- Experience with NLP libraries (spaCy, NLTK, Hugging Face Transformers)
- Proficiency in Python and machine learning frameworks (TensorFlow, PyTorch)
- Knowledge of deep learning models (RNNs, BERT, LSTMs)
- Research mindset and passion for language technologies

Responsibilities:
Design, develop, and implement advanced Natural Language Processing (NLP) models and applications.
Utilize leading NLP libraries such as spaCy, NLTK, and Hugging Face Transformers for various tasks.
Build and train deep learning models (RNNs, BERT, LSTMs) using TensorFlow or PyTorch frameworks.
Conduct research and experimentation to improve the performance and capabilities of NLP systems.
Collaborate with other AI engineers and product teams to integrate NLP solutions into intelligent systems.
""",
                company="CogniTech AI",
                location="Istanbul, Turkey",
                salary="₺100,000 - ₺160,000 per month",
                required_skills="NLP, spaCy, NLTK, Hugging Face Transformers, Python, TensorFlow, PyTorch, Deep Learning"
            ),

            Job(
                title="Junior Front-End Developer – React.js",
                description="""
We are looking for a Junior Front-End Developer to build interactive web applications using React.

Qualifications:
- Bachelor’s degree in Computer Engineering or related field
- Basic understanding of JavaScript, HTML, CSS
- Familiarity with React.js and component-based architecture
- Willingness to learn and improve UI/UX skills
- Team-oriented and good communication skills

Responsibilities:
Develop and maintain user-facing features for web applications using React.js.
Write clean, efficient, and well-structured code in JavaScript, HTML, and CSS.
Collaborate with senior developers and designers to translate UI/UX designs into functional components.
Participate in code reviews and contribute to the continuous improvement of coding standards.
Actively learn new front-end technologies and best practices to enhance development skills.
""",
                company="Web Innovations",
                location="Ankara, Turkey",
                salary="₺45,000 - ₺70,000 per month",
                required_skills="JavaScript, HTML, CSS, React.js, UI/UX"
            ),

            Job(
                title="DevOps Engineer – Cloud Infrastructure",
                description="""
Join our DevOps team to automate and maintain cloud-based deployment pipelines.

Qualifications:
- Bachelor’s in Computer Engineering or Information Systems
- Experience with CI/CD tools (Jenkins, GitHub Actions)
- Knowledge of Docker, Kubernetes, and infrastructure as code (Terraform, Ansible)
- Familiarity with monitoring tools (Prometheus, Grafana)
- Strong scripting skills (Bash, Python)

Responsibilities:
Design, implement, and maintain CI/CD pipelines using tools like Jenkins or GitHub Actions to automate software delivery.
Manage and optimize cloud infrastructure using Docker and Kubernetes for container orchestration.
Develop and maintain infrastructure as code (IaC) using Terraform or Ansible for consistent and repeatable deployments.
Set up and manage monitoring and alerting systems with tools like Prometheus and Grafana.
Automate operational tasks and improve system reliability through scripting (Bash, Python).
""",
                company="CloudOps Solutions",
                location="Istanbul, Turkey",
                salary="₺90,000 - ₺145,000 per month",
                required_skills="CI/CD, Jenkins, GitHub Actions, Docker, Kubernetes, Terraform, Ansible, Prometheus, Grafana, Bash, Python"
            ),
            Job(
                title="Human Resources Assistant (Entry-Level)",
                description="""
Support daily Human Resources operations, assist in recruitment tasks, and contribute to employee onboarding in a fast-paced HR department.

Qualifications:

- Currently pursuing or recently graduated with a degree in Labor Economics, Industrial Relations, or related field
- Completed internship experience in HR or administration
- Familiar with resume screening, data entry, and employee orientation support
- Proficient in MS Office (Excel, Word, PowerPoint)
- Strong communication, attention to detail, and teamwork skills
- Intermediate English and native Turkish

Responsibilities:
Assist with various daily HR operations, ensuring smooth departmental functioning.
Support the recruitment process by posting job ads, screening resumes, and scheduling interviews.
Prepare and organize HR documents, including employee records and new hire paperwork.
Perform accurate data entry and maintain HR databases.
Contribute to employee onboarding by assisting with orientation sessions and preparing welcome materials.
Provide general administrative support to the HR team.
""", 
                company="NeoPeople Consulting", 
                location="Istanbul, Turkey", 
                salary="₺28,000 - ₺38,000 per month", 
                required_skills="Recruitment Support, Data Entry, Filing, Communication, Teamwork, MS Office"
            ),
            Job(
                title="Logistics Specialist",
                description="""
We are seeking a highly motivated and results-oriented Logistics Specialist with a strong background in supply chain management, warehouse operations, and distribution processes. The ideal candidate will be adept at managing complex logistics operations, optimizing transportation, and driving cost reduction initiatives. This role requires a professional with proven expertise in inventory management and a commitment to continuous improvement.

Key Responsibilities:

- Manage and optimize end-to-end supply chain operations to ensure timely and efficient delivery.
- Oversee warehouse operations, including inventory control, storage, and order fulfillment.
- Develop and implement strategies for transportation optimization and cost reduction.
- Negotiate with carriers and suppliers to secure favorable terms and improve service quality.
- Monitor and analyze logistics Key Performance Indicators (KPIs) to identify areas for improvement.
- Implement and manage logistics software (WMS, TMS) for enhanced operational efficiency.
- Collaborate with internal teams to ensure smooth coordination between logistics and other departments.
- Proactively identify and resolve supply chain disruptions.

Qualifications:

- Bachelor's degree in Logistics Management, Supply Chain Management, Business Administration, or a related field.
- Minimum of 5 years of proven experience in logistics, supply chain, warehouse, or distribution management.
- Strong proficiency in inventory management, transportation optimization, and cost reduction strategies.
- Demonstrated experience in improving operational efficiency and implementing continuous improvement projects.
- Familiarity with logistics software (WMS, TMS) is a plus.
- Excellent analytical, problem-solving, and negotiation skills.
- Strong communication and interpersonal skills.
- Fluent in English; knowledge of additional languages is a plus.
""",
                company="Global Supply Solutions Inc.",
                location="Istanbul, Turkey",
                salary="₺50,000 - ₺75,000 per month",
                required_skills="Supply Chain Management, Warehouse Operations, Distribution Processes, Inventory Management, Transportation Optimization, Cost Reduction, Logistics KPIs, WMS, TMS, Continuous Improvement"
            ),
            Job(
                title="Mobile Developer – iOS/Android",
                description="""
We are seeking a Mobile Developer to create high-quality mobile apps for Android and iOS.

Qualifications:
- Bachelor’s in Computer Engineering or similar field
- Proficiency in Swift or Kotlin
- Experience with mobile frameworks (Flutter, React Native is a plus)
- Strong understanding of mobile UI design principles
- Familiarity with API integration and mobile performance optimization

Responsibilities:
Design, develop, and maintain high-performance mobile applications for both Android and iOS platforms using Swift or Kotlin.
Utilize mobile development frameworks like Flutter or React Native (if applicable) to build cross-platform solutions.
Implement intuitive and user-friendly mobile UI designs, ensuring a seamless user experience.
Integrate with various APIs and backend services to fetch and display data.
Optimize mobile applications for maximum performance, responsiveness, and scalability.
Collaborate with designers, product managers, and other developers to deliver robust and engaging mobile products.

""",
                company="MobileCraft Studios",
                location="Izmir, Turkey",
                salary="₺85,000 - ₺130,000 per month",
                required_skills="Swift, Kotlin, Flutter, React Native, Mobile UI/UX, API Integration"
            ),

            Job(
                title="Operations Manager – Manufacturing",
                description="""
Oversee daily manufacturing operations, ensuring efficiency, quality, and adherence to production schedules.

Qualifications:

-Bachelor’s degree in Engineering, Operations Management, or a related field
-5+ years of experience in a manufacturing operations role, with 2+ years in management
-Strong knowledge of Lean Manufacturing and Six Sigma principles
-Excellent leadership and problem-solving skills
-Experience with production planning and inventory management 

Responsibilities:
Direct and manage all daily manufacturing operations, ensuring efficiency and optimal resource utilization.
Implement and enforce quality control standards to meet production specifications and customer expectations.
Develop and monitor production schedules, ensuring timely delivery and adherence to targets.
Apply Lean Manufacturing and Six Sigma methodologies to identify and eliminate waste, improving overall operational performance.
Oversee inventory management, optimizing stock levels and material flow.
Lead, mentor, and motivate manufacturing teams to foster a culture of continuous improvement and high performance.

""", 
                company="Precision Manufacturing Co.", 
                location="Istanbul, Turkey", 
                salary="₺80,000 - ₺130,000 per month", 
                required_skills="Operations Management, Manufacturing, Lean Manufacturing, Six Sigma, Production Planning, Inventory Management"
            ),

            Job(
                title="Machine Learning Engineer – Recommender Systems",
                description="""
We are hiring a Machine Learning Engineer to design recommendation engines for our platform.

Qualifications:
- Master’s or Bachelor’s in Computer Engineering or Data Science
- Proficiency in Python and ML libraries (scikit-learn, LightGBM, XGBoost)
- Experience with collaborative filtering, matrix factorization, or deep learning models
- Good understanding of evaluation metrics (RMSE, MAP, precision@k)
- Ability to work with large-scale data

Responsibilities:
Design, develop, and deploy recommender systems using various machine learning techniques.
Implement and fine-tune models such as collaborative filtering, matrix factorization, and deep learning models to improve recommendation accuracy.
Utilize Python and relevant ML libraries like scikit-learn, LightGBM, and XGBoost for model development.
Evaluate the performance of recommendation engines using metrics like RMSE, MAP.
Work with large-scale datasets to train and validate models, ensuring scalability and efficiency.
Collaborate with data scientists and product teams to integrate recommendation systems into the platform and drive business value.


""",
                company="Recommendation AI",
                location="Istanbul, Turkey",
                salary="₺95,000 - ₺155,000 per month",
                required_skills="Python, Scikit-learn, LightGBM, XGBoost, Collaborative Filtering, Deep Learning, Recommender Systems"
            ),
            Job(
                title="Architect – Design and Project Execution",
                description="""
We are looking for a talented Architect to join our dynamic team, focusing on residential and commercial architectural design. The ideal candidate will be responsible for preparing architectural drawings, coordinating with project stakeholders, and overseeing construction processes.

Qualifications:
- Bachelor’s degree in Architecture
- Minimum 2 years of experience in architectural design and application projects
- Proficiency in AutoCAD, Revit, SketchUp, and Lumion
- Familiarity with Adobe Photoshop and InDesign is a plus
- Strong understanding of technical drawing standards and building regulations
- Excellent communication and time management skills
- Ability to work collaboratively within interdisciplinary teams

Responsibilities:
Develop and prepare comprehensive architectural drawings and design documents for residential and commercial projects.
Utilize AutoCAD, Revit, SketchUp, and Lumion to create detailed designs, models, and visualizations.
Coordinate with project stakeholders, including clients, engineers, contractors, and local authorities, throughout the project lifecycle.
Oversee construction processes, ensuring adherence to design specifications, quality standards, and building regulations.
Conduct site visits to monitor progress, address design-related issues, and provide technical guidance.
Contribute to all phases of design and project execution, from conceptualization to completion.

""",
                company="Nova Architecture & Construction Ltd.",
                location="Istanbul, Turkey",
                salary="₺75,000 - ₺110,000 per month",
                required_skills="AutoCAD, Revit, SketchUp, Lumion, Adobe Photoshop, Technical Drawing, Project Coordination"
            ),
            Job(
                title="Senior Human Resources Manager – Strategic HR Leadership",
                description="""
We are looking for a highly experienced and forward-thinking Senior Human Resources Manager to lead and evolve our HR strategies in alignment with our organizational goals. This role requires a seasoned HR leader who can oversee multiple HR functions, build a strong company culture, and act as a strategic partner to senior leadership.

Qualifications:
- Bachelor’s or Master’s degree in Human Resources, Business Administration, Organizational Psychology, or a related field
- At least 7 years of progressive experience in human resources, with proven team leadership
- Strong command of labor laws, employee relations, and organizational development
- Demonstrated expertise in talent acquisition, performance management, learning & development, and employee engagement
- Experience with HR analytics, KPI reporting, and HRIS tools (e.g., SAP, Workday, BambooHR)
- Excellent interpersonal, leadership, and strategic thinking skills
- Fluency in English (Turkish proficiency is a plus)

Responsibilities:
- Lead the strategic planning and execution of all HR functions across the organization
- Act as a key advisor to senior executives on people-related matters
- Manage and mentor the HR team to ensure continuous improvement and professional development
- Oversee talent management processes including recruitment, onboarding, succession planning, and retention
- Drive initiatives related to DEI (Diversity, Equity, and Inclusion), organizational culture, and employee satisfaction
- Monitor HR compliance and ensure alignment with legal requirements and internal policies
- Develop HR metrics and use data to support decisions and drive improvements

""",
                company="Orbis Group",
                location="Istanbul, Turkey",
                salary="₺90,000 - ₺130,000 per month",
                required_skills="Strategic HR, Talent Management, Leadership, Organizational Development, Performance Systems, Labor Law, HR Analytics, Employee Engagement"
            ),

            Job(
                title="Industrial Engineer – Process Optimization",
                description="""
We are seeking an Industrial Engineer to streamline production workflows and improve operational efficiency in our manufacturing plant.

Qualifications:
- BSc in Industrial Engineering
- Strong knowledge of lean manufacturing and Six Sigma
- Experience with ERP systems and data analysis tools
- Ability to lead process improvement projects

Responsibilities:
Analyze existing production workflows to identify inefficiencies and bottlenecks.
Design and implement process improvement projects using Lean Manufacturing and Six Sigma methodologies to enhance operational efficiency.
Utilize data analysis tools and insights from ERP systems to make informed recommendations for optimization.
Collaborate with various departments to ensure the successful execution of process changes and new initiatives.
Monitor and evaluate the performance of implemented improvements, reporting on key metrics and sustained gains.
""",
                company="OptiFactory",
                location="Gebze, Turkey",
                salary="₺65,000 - ₺95,000 per month",
                required_skills="Lean Manufacturing, Six Sigma, ERP, Data Analysis"
            ),

            Job (
                title="Senior Frontend Developer",
                description="""
We're looking for a Senior Frontend Developer to lead the development of user-facing features for our web applications.

Qualifications:

-Bachelor’s in Computer Science or related field
-5+ years of experience with React, Angular, or Vue.js
-Strong understanding of HTML5, CSS3, and JavaScript (ES6+)
-Experience with RESTful APIs and modern build tools (Webpack, Babel)
-Portfolio of strong UI/UX implementations 

Responsibilities:
Lead the design, development, and implementation of complex, user-facing features for web applications.
Utilize expertise in React, Angular, or Vue.js to build high-performance and scalable frontend solutions.
Write clean, efficient, and well-structured code using HTML5, CSS3, and modern JavaScript (ES6+).
Integrate with RESTful APIs and ensure seamless data flow between frontend and backend systems.
Employ modern build tools like Webpack and Babel to optimize development workflows and application performance.
Collaborate closely with UI/UX designers, backend developers, and product managers to deliver exceptional user experiences.
Mentor junior developers and contribute to best practices in frontend development.
""", 
                company="Innovatech", 
                location="Istanbul, Turkey", 
                salary="₺85,000 - ₺130,000 per month", 
                required_skills="React, Angular, Vue.js, HTML5, CSS3, JavaScript, RESTful APIs, Webpack"
            ),

            

            Job(
                title="Product Manager – Mobile Applications",
                description="""
Lead the product lifecycle for our mobile applications, from ideation to launch and iteration.

Qualifications:

-Bachelor’s degree in Business, Computer Science, or a related field
-4+ years of product management experience, preferably with mobile apps
-Strong understanding of Agile methodologies
-Excellent communication, leadership, and problem-solving skills
-Experience with user research and A/B testing 

Responsibilities:
Define and champion the product vision, strategy, and roadmap for our mobile applications.
Lead the entire product lifecycle, from ideation and requirements gathering to launch and post-launch iteration.
Translate business needs into detailed product requirements and user stories.
Work closely with engineering, design, and marketing teams within an Agile framework to deliver high-quality mobile apps.
Conduct user research, market analysis, and A/B testing to inform product decisions and identify opportunities for improvement.
Monitor and analyze product performance, using data to drive strategic enhancements and achieve key business objectives.
""", 
                company="App Innovations Inc.", 
                location="Istanbul, Turkey", 
                salary="₺95,000 - ₺150,000 per month", 
                required_skills="Product Management, Mobile Apps, Agile, User Research, A/B Testing" 
            ),

            Job(
                title="Business Analyst – IT Projects",
                description="""
We are hiring a Business Analyst to gather requirements, document specifications, and act as a bridge between business and technical teams.

Qualifications:
- Degree in MIS, Business, or Engineering
- 2+ years in business analysis or project coordination
- Experience with Agile methodologies
- Excellent communication and documentation skills

Responsibilities:
Gather and analyze business requirements from stakeholders, translating them into clear and detailed functional and non-functional specifications for IT projects.
Document system requirements, use cases, and process flows, ensuring accuracy and completeness.
Act as a vital bridge between business stakeholders and technical development teams, facilitating effective communication and understanding.
Participate actively in Agile ceremonies (e.g., sprint planning, stand-ups, retrospectives) to support project delivery.
Conduct testing and validation of implemented solutions to ensure they meet business needs and quality standards.
""",
                company="SoftLine Solutions",
                location="Istanbul, Turkey",
                salary="₺70,000 - ₺105,000 per month",
                required_skills="Business Analysis, Requirements Gathering, Agile, Communication"
            ),
           
            Job(
                title="QA Engineer – Automation Testing",
                description="""
We're hiring a QA Engineer to develop and execute automated tests for our web applications.

Qualifications:
- Degree in Computer Engineering or similar
- Knowledge of Selenium, Cucumber, and Jenkins
- Experience in API testing and CI/CD pipelines
- Attention to detail and problem-solving mindset

Responsibilities:
Design, develop, and maintain automated test scripts for web applications using tools like Selenium and Cucumber.
Execute automated test suites and analyze test results to identify defects and ensure software quality.
Perform API testing to validate backend functionalities and integrations.
Integrate automated tests into CI/CD pipelines using tools such as Jenkins to support continuous integration and delivery.
Collaborate with development teams to understand new features and ensure comprehensive test coverage.
Report and track bugs, working with developers to facilitate timely resolution.
""",
                company="TestBridge",
                location="Ankara, Turkey",
                salary="₺70,000 - ₺100,000 per month",
                required_skills="Selenium, API Testing, CI/CD, Automation Testing"
            ),

            Job(
                title="Senior Financial Analyst – Corporate Finance & Strategy",
                description="""
We are looking for a highly analytical and detail-oriented Senior Financial Analyst to join our corporate finance team. The ideal candidate will bring hands-on experience in financial modeling, forecasting, reporting, and investment analysis, supporting executive decision-making through data-driven insights.

Qualifications:
- Bachelor’s degree in Finance, Business Administration, Economics, or a related field
- Minimum 3 years of experience in financial analysis or corporate finance
- Advanced skills in financial modeling (DCF, Comparable Analysis), budgeting, and forecasting
- Strong command of financial reporting tools and variance analysis
- Proficiency in MS Excel (advanced), PowerPoint, and Bloomberg Terminal or SAP FI (a plus)
- Experience with risk analysis and investment project feasibility studies
- Strong analytical thinking and ability to simplify complex financial data
- Excellent communication and presentation skills
- Fluent in English (written and spoken)

Responsibilities:
- Build and maintain complex financial models to support strategic planning and investment decisions
- Prepare detailed financial performance reports and variance analyses for senior leadership
- Lead budgeting and forecasting processes across business units
- Conduct feasibility and risk analyses for new investment projects
- Provide actionable insights and financial recommendations based on data analysis
- Collaborate with cross-functional teams including strategy, accounting, and operations
- Ensure accuracy and consistency in financial data management and reporting
""",
                company="Altin Capital Partners",
                location="Istanbul, Turkey",
                salary="₺85,000 - ₺120,000 per month (depending on experience)",
                required_skills="Financial Modeling, Forecasting, Reporting, Excel, Risk Analysis, DCF, Investment Feasibility, Bloomberg, SAP FI, Data Analysis"
            ),
            Job(
                title="Research Scientist – Biotechnology",
                description="""
Conduct innovative research and experiments in the field of biotechnology, contributing to new discoveries.

Qualifications:

-PhD in Biotechnology, Molecular Biology, Biochemistry, or a related field
-3+ years of postdoctoral or industry research experience
-Strong background in experimental design and data analysis
-Excellent publication record is a plus
-Proficiency in lab techniques relevant to biotechnology 

Responsibilities:
Design and execute innovative research experiments in the field of biotechnology to drive new discoveries and product development.
Apply a strong background in experimental design to ensure robust and reproducible results.
Perform advanced lab techniques specific to molecular biology, biochemistry, or other relevant biotechnology areas.
Analyze and interpret complex data, drawing meaningful conclusions and identifying future research directions.
Prepare scientific reports, presentations, and contribute to publications in peer-reviewed journals.
Collaborate with interdisciplinary teams to translate research findings into tangible applications.
""", 
                company="BioGen Innovations", 
                location="Istanbul, Turkey", 
                salary="₺95,000 - ₺155,000 per month", 
                required_skills="Biotechnology, Molecular Biology, Biochemistry, Research, Experimental Design, Lab Techniques"                 
            ),

            Job(
                title="Interior Architect – Residential Projects",
                description="""
Seeking an Interior Architect to design creative and functional residential spaces.

Qualifications:
- Degree in Interior Architecture or related field
- Proficiency in SketchUp, 3ds Max, and AutoCAD
- Portfolio in home or residential projects
- Strong sense of aesthetics and material selection

Responsibilities:
Develop creative and functional interior designs for residential projects, from concept to completion.
Produce detailed architectural drawings and 3D visualizations using SketchUp, 3ds Max, and AutoCAD.
Select appropriate materials, finishes, and furnishings, considering both aesthetics and practicality.
Collaborate closely with clients to understand their needs and preferences, ensuring designs meet their vision.
Oversee project execution, coordinating with contractors and suppliers to ensure design integrity and quality.
""",
                company="DecoArt",
                location="Antalya, Turkey",
                salary="₺55,000 - ₺85,000 per month",
                required_skills="Interior Design, SketchUp, AutoCAD, 3ds Max"
            ),
            Job(
                title="Software Developer Intern – Summer Internship Program",
                description="""
We are seeking a motivated and detail-oriented Software Developer Intern to join our team for the summer internship period. The ideal candidate will support the development team in building and maintaining software applications, with a focus on object-oriented programming, database management, and modern software technologies.

Qualifications:
- Currently pursuing a Bachelor's degree in Computer Engineering or a related field (3rd or 4th year)
- Familiarity with Java, Python, or .NET programming languages
- Basic knowledge of relational databases such as MySQL or MSSQL
- Understanding of Object-Oriented Programming (OOP) principles
- Interest in Data Science and Artificial Intelligence is a plus
- Strong analytical and problem-solving skills
- Ability to work effectively within a team
- English proficiency at B2 level or higher

Internship Details:
- Duration: 40 working days
- Location: Istanbul (hybrid work options available)
- Opportunity to work on real-world projects and gain hands-on experience in a professional development environment
""",
                company="InnovateTech Software Solutions",
                location="Istanbul, Turkey",
                salary="Unpaid Internship (with potential for part-time offer post-internship)",
                required_skills="Java, Python, .NET, MySQL, MSSQL, OOP, Teamwork, English B2"
            ),

            Job(
                title="Supply Chain Coordinator",
                description="""
Manage the flow of goods and services, ensuring efficient and timely delivery from suppliers to customers.

Qualifications:

-Bachelor’s degree in Supply Chain Management, Logistics, or a related field
-2+ years of experience in supply chain operations
-Strong organizational and analytical skills
-Proficiency in supply chain software (e.g., ERP systems)
-Excellent negotiation and communication skills 

Responsibilities:
Coordinate and monitor the entire supply chain process, from procurement to delivery, to ensure efficiency and timeliness.
Manage relationships with suppliers and vendors, including contract negotiation and performance evaluation.
Utilize ERP systems and other supply chain software to track inventory, orders, and shipments.
Analyze supply chain data to identify areas for improvement and implement optimization strategies.
Communicate effectively with internal teams and external partners to resolve any issues and ensure smooth operations.
""", 
                company="Logistics Masters", 
                location="Istanbul, Turkey", 
                salary="₺48,000 - ₺75,000 per month", 
                required_skills="Supply Chain, Logistics, ERP, Negotiation"
            ),

            Job(
                title="Legal Counsel",
                description="""
Provide legal advice and support to various departments, ensuring compliance with local and international laws.

Qualifications:

-Law degree from a reputable university
-Admitted to the Bar (Turkey)
-5+ years of experience in corporate law, preferably in a corporate setting
-Strong understanding of contract law, intellectual property, and data privacy
-Excellent analytical and drafting skills 

Responsibilities:
Provide comprehensive legal advice and support to various internal departments on a wide range of legal matters.
Ensure the company's full compliance with local and international laws and regulations, minimizing legal risks.
Draft, review, and negotiate various legal documents, including contracts, agreements, and policies.
Manage and protect the company's intellectual property rights.
Advise on data privacy regulations and best practices, ensuring adherence to relevant laws like GDPR or KVKK.
Conduct legal research and analysis to support strategic business decisions and resolve legal issues.
""", 
                company="Corporate Law Firm", 
                location="Istanbul, Turkey", 
                salary="₺110,000 - ₺180,000 per month", 
                required_skills="Corporate Law, Contract Law, Intellectual Property, Data Privacy, Legal Drafting"
            ),

            Job(
                title="Customer Support Representative",
                description="""
Deliver exceptional customer service by addressing inquiries, resolving issues, and ensuring customer satisfaction.

Qualifications:

-High school diploma or equivalent; Bachelor’s degree preferred
-1+ year of experience in customer support or a related field
-Excellent verbal and written communication skills
-Strong problem-solving abilities and empathy
-Proficiency with CRM software

Responsibilities:
Respond promptly and professionally to customer inquiries via phone, email, and chat.
Resolve customer issues and complaints efficiently, escalating complex problems when necessary.
Document all customer interactions and resolutions accurately in the CRM software.
Provide product or service information and assist customers with their needs.
Maintain a high level of customer satisfaction by delivering empathetic and effective support.
""", 
                company="Service Excellence", 
                location="Istanbul, Turkey", 
                salary="₺35,000 - ₺50,000 per month", 
                required_skills="Customer Service, Communication, Problem Solving, CRM" 
            ),

            Job(
                title="UX/UI Designer",
                description="""
Design intuitive and engaging user experiences for our digital products, from wireframes to high-fidelity prototypes.

Qualifications:

-Bachelor’s degree in Design, Human-Computer Interaction, or a related field
-3+ years of experience in UX/UI design
-Proficiency with design tools (Figma, Sketch, Adobe XD)
-Strong portfolio demonstrating UX research and UI design skills
-Understanding of user-centered design principles 

Responsibilities:
Conduct user research to understand user behaviors, needs, and motivations.
Translate research insights into intuitive user flows, wireframes, and interactive prototypes.
Design visually appealing and functional user interfaces (UI) for digital products, ensuring a consistent brand experience.
Utilize design tools like Figma, Sketch, or Adobe XD to create and iterate on designs.
Collaborate closely with product managers and developers to ensure design feasibility and successful implementation.
Conduct usability testing and iterate on designs based on user feedback and data analysis.
""", 
                company="Design Forward Studio", 
                location="Istanbul, Turkey", 
                salary="₺60,000 - ₺95,000 per month", 
                required_skills="UX Design, UI Design, Figma, Sketch, Adobe XD, User Research, Prototyping"   
            ),

            Job(
                title="Sales Executive – B2B Solutions",
                description="""
Looking for a Sales Executive to grow our enterprise client base and close new deals.

Qualifications:
- Degree in Business or Marketing
- Experience in B2B sales and CRM systems
- Negotiation and client relationship skills
- Ability to meet and exceed sales targets

Responsibilities:

Identify and pursue new B2B sales opportunities to expand the enterprise client base.
Manage the entire sales cycle, from lead generation and prospecting to closing deals.
Build and maintain strong client relationships, understanding their needs and offering tailored solutions.
Utilize CRM systems to track sales activities, manage pipelines, and report on progress.
Consistently meet and exceed assigned sales targets and quotas.
Prepare and deliver compelling sales presentations and proposals to prospective clients.
""",
                company="TradePlus",
                location="Bursa, Turkey",
                salary="₺60,000 - ₺100,000 per month + bonus",
                required_skills="B2B Sales, CRM, Negotiation, Communication"
            ),

            Job(
                    title="Environmental Engineer – Compliance & Reporting",
                    description="""
We need an Environmental Engineer to ensure regulatory compliance and conduct environmental impact assessments.

Qualifications:
- BSc in Environmental Engineering
- Familiarity with Turkish and EU environmental laws
- Experience with EIA and sustainability practices
- Report writing and data analysis skills

Responsibilities:
Ensure adherence to all Turkish and EU environmental laws and regulations for company operations.
Conduct thorough Environmental Impact Assessments (EIA) for new projects and existing facilities.
Develop and prepare comprehensive environmental reports, including compliance documents and sustainability metrics.
Analyze environmental data to identify potential risks and recommend corrective actions.
Implement and promote sustainability practices across the organization to minimize environmental footprint.
Collaborate with internal teams and external agencies on environmental permitting and licensing processes.
""",
                    company="EcoTrack",
                    location="Gaziantep, Turkey",
                    salary="₺55,000 - ₺85,000 per month",
                    required_skills="Environmental Compliance, EIA, Sustainability, Reporting"
            ),

            Job(
                title="IT Support Specialist",
                description="""
Provide technical support to employees, troubleshoot hardware and software issues, and manage IT infrastructure.

Qualifications:

-Associate's or Bachelor’s degree in Information Technology or a related field
-2+ years of experience in IT support
-Strong knowledge of Windows and macOS operating systems
-Familiarity with network troubleshooting and hardware maintenance
-Excellent communication and problem-solving skills 

Responsibilities:
Provide first-line technical support to employees, resolving hardware and software issues efficiently.
Troubleshoot problems related to operating systems (Windows, macOS), applications, and peripherals.
Perform hardware maintenance and upgrades, ensuring all equipment functions optimally.
Assist with network troubleshooting, identifying and resolving connectivity issues.
Manage user accounts, permissions, and other aspects of IT infrastructure.
Document support tickets and resolutions, maintaining clear records of all technical assistance provided.
""", 
                company="Tech Solutions Hub", 
                location="Istanbul, Turkey", 
                salary="₺40,000 - ₺60,000 per month", 
                required_skills="IT Support, Windows, macOS, Network Troubleshooting, Hardware" 
            ),
            Job(
                title="Sales Representative – B2B Field Services",
                description="""
We are looking for a dynamic and client-focused Sales Representative to drive business growth through face-to-face engagement with our corporate clients. This role is ideal for professionals with a passion for sales, excellent communication skills, and a solid understanding of B2B service offerings.

Key Responsibilities:

- Generate leads and expand the customer base through field visits, referrals, and local networking
- Conduct client meetings to present company services and develop tailored proposals
- Maintain regular communication with existing clients to ensure satisfaction and upsell opportunities
- Collaborate with marketing and customer success teams to align outreach strategies
- Keep accurate records of client interactions and deals in CRM software (e.g., HubSpot)
- Attend industry events and trade shows to represent the company and develop new business
- Monitor market trends and report competitor activities to the sales director

Qualifications:

- Bachelor’s degree in Business, Marketing, or Communication
- Minimum 2 years of field sales or client-facing B2B sales experience
- Familiarity with B2B services (consulting, HR solutions, IT outsourcing, etc.)
- Hands-on experience with CRM tools like HubSpot or Zoho
- Excellent interpersonal and communication skills, with a proactive mindset
- Valid driver’s license and willingness to travel for on-site client meetings
- Fluent in English and Turkish

""",
                company="NextGen Business Services",
                location="Ankara, Turkey (On-site & Field-Based)",
                salary="₺40,000 - ₺60,000 per month + Performance Bonus",
                required_skills="B2B Sales, Field Visits, HubSpot CRM, Client Relationship Building, Proposal Development, Communication, Business Networking, Customer Retention"
            ),
            Job(
                title="Logistics Coordinator – Operational Support & Execution",
                description="""
We are looking for an organized and motivated Logistics Coordinator to support our day-to-day logistics operations. This role is ideal for a candidate with a solid understanding of basic logistics principles who is eager to grow their career in a dynamic and fast-paced supply chain environment.

Key Responsibilities:

- Assist in planning and tracking shipments, ensuring timely and accurate deliveries
- Coordinate with transport companies and warehouses for pick-ups and dispatches
- Prepare shipping documents and maintain accurate logistics records
- Monitor stock levels and support basic inventory control processes
- Communicate effectively with internal departments such as sales and procurement
- Help resolve shipping or delivery issues as they arise
- Support import/export operations under the guidance of senior team members

Qualifications:

- Bachelor's degree in Logistics, Business Administration, or related fields
- Minimum 2 years of experience in logistics, supply chain, or transportation
- Basic understanding of shipping documentation, warehousing, and inventory
- Familiarity with logistics software or ERP systems is a plus (training will be provided)
- Good organizational and communication skills
- Proficiency in English (written and spoken)

""",
                company="NovaLine Logistics Co.",
                location="Bursa, Turkey",
                salary="₺35,000 - ₺50,000 per month",
                required_skills="Logistics Coordination, Shipping Documentation, Inventory Support, Transportation Planning, Communication, Problem Solving, MS Excel, Import/Export Basics"
            ),

            Job(
                title="Content Writer – Tech Niche",
                description="""
Create compelling and informative content for our tech blog, website, and marketing materials.

Qualifications:

Bachelor’s degree in Journalism, English, Marketing, or a related field
2+ years of experience in content writing, preferably in the tech industry
Strong research skills and ability to explain complex technical concepts clearly
Excellent grammar, punctuation, and style
Familiarity with SEO content strategies 

Responsibilities:
Develop and write high-quality, engaging, and informative content for our tech blog, website, and various marketing materials.
Conduct thorough research on technical topics and industry trends to ensure accuracy and relevance.
Translate complex technical concepts into clear, concise, and accessible language for a diverse audience.
Implement SEO content strategies to improve search engine ranking and drive organic traffic.
Edit and proofread content to ensure impeccable grammar, punctuation, and style.
Collaborate with marketing, product, and other teams to align content with overall business objectives.
""", 
                company="Digital Content Creators", 
                location="Istanbul, Turkey", 
                salary="₺38,000 - ₺58,000 per month", 
                required_skills="Content Writing, Tech Writing, SEO, Research, Grammar, Blog Writing" 
            ),
            
            Job(
                title="Industrial Designer – Consumer Products",
                description="""
We are hiring an Industrial Designer to create ergonomic and aesthetically pleasing consumer product designs.

Qualifications:
- Bachelor's in Industrial Design or Product Design
- Proficiency in Rhino, SolidWorks, or KeyShot
- Strong portfolio in physical product design
- Creative mindset and teamwork skills

Responsibilities:
Design and develop ergonomic and aesthetically pleasing consumer products from concept to production.
Create 3D models, renderings, and technical drawings using software such as Rhino, SolidWorks, or KeyShot.
Collaborate with engineering and marketing teams to ensure designs are feasible, cost-effective, and meet market demands.
Conduct research on user needs, market trends, and material innovations to inform design decisions.
Present design concepts and prototypes to stakeholders, gathering feedback and iterating as needed.
""",
                company="ErgoStudio",
                location="Istanbul, Turkey",
                salary="₺65,000 - ₺95,000 per month",
                required_skills="Industrial Design, SolidWorks, Rhino, Product Aesthetics"
            ),
            Job(
                title="Interior Architecture Director – Creative and Sustainable Design",
                description="""
We are looking for an experienced and visionary Interior Architecture Director to lead innovative design projects across residential, commercial, and retail spaces. The ideal candidate will bring a strong aesthetic sensibility, deep knowledge of sustainable design principles, and outstanding leadership skills to deliver functional and visually striking environments.

Qualifications:
- Master’s degree in Interior Architecture or related field
- Minimum 7 years of professional experience in interior design and architecture
- Proven ability to lead teams and manage large-scale design projects
- Proficiency in AutoCAD, SketchUp, V-Ray, and Adobe Creative Suite (Photoshop, InDesign)
- Strong understanding of sustainable design, materials, and LEED principles
- Excellent communication and client relationship management skills
- Fluent in English and Turkish

Responsibilities:
- Lead the concept, design, and execution phases of interior architecture projects
- Manage and mentor multidisciplinary design teams
- Oversee client communications and ensure project goals are met on time and within budget
- Implement environmentally conscious design solutions
- Coordinate with suppliers, monitor site implementation, and ensure design quality

""",
                company="ArtiSpace Design Studio",
                location="Istanbul, Turkey",
                salary="₺110,000 - ₺160,000 per month",
                required_skills="Interior Design, Project Management, AutoCAD, SketchUp, V-Ray, LEED, Sustainable Design, Team Leadership"
            ),

            Job(
                title="Senior Full-Stack Developer – Web Applications",
                description="""
We are seeking a Senior Full-Stack Developer to lead web development projects end-to-end.

Qualifications:
- Bachelor’s or Master’s in Computer Engineering
- 5+ years of experience in full-stack development
- Expertise in .NET Core, JavaScript, Angular/React, and SQL
- Knowledge of design patterns, testing, and scalable architecture
- Strong leadership and mentoring capabilities

Responsibilities:
Lead the design, development, and deployment of full-stack web applications from conception to completion.
Develop robust backend services using .NET Core and integrate with SQL databases.
Build dynamic and responsive user interfaces with JavaScript and modern frontend frameworks like Angular or React.
Apply best practices in design patterns and scalable architecture to ensure high performance and maintainability.
Conduct code reviews, provide technical guidance, and mentor junior developers.
Collaborate with cross-functional teams to define requirements, set technical standards, and ensure successful project delivery.
""",
                company="Enterprise Web Solutions",
                location="Ankara, Turkey",
                salary="₺110,000 - ₺180,000 per month",
                required_skills=".NET Core, JavaScript, Angular, React, SQL, Design Patterns, Scalable Architecture"
            ),
            Job(
                title="Senior R&D Specialist – Biotechnology and Pharmaceutical Research",
                description="""
We are seeking a highly skilled and motivated Senior R&D Specialist to join our pharmaceutical biotechnology research team. The ideal candidate will bring extensive experience in molecular biology, genetic engineering, and drug discovery processes. This role involves conducting laboratory experiments, performing data analysis, and supporting the development of innovative therapeutic solutions in compliance with GMP and GLP standards.

Qualifications:
- Master's degree in Molecular Biology, Genetics, Biotechnology, or a related field
- At least 5 years of experience in R&D roles within the pharmaceutical or biotechnology sector
- Proficient in laboratory techniques including PCR, qPCR, Western Blot, ELISA, and protein purification
- Hands-on experience with genetic engineering methods (e.g., CRISPR/Cas9)
- Strong knowledge of cell culture and sterile lab techniques
- Competence in data analysis, statistics, and the use of bioinformatics tools (e.g., NCBI, BLAST)
- Skilled in scientific reporting, documentation, and GMP/GLP compliance
- Experience mentoring junior team members and managing lab operations
- Excellent command of MS Office (Excel, PowerPoint) for reporting and presentations

Responsibilities:
- Lead and conduct laboratory experiments in molecular biology and drug development
- Design and execute gene expression studies and protein characterization experiments
- Analyze and interpret scientific data, contributing to strategic decision-making
- Ensure laboratory operations meet GMP and GLP standards
- Collaborate with cross-functional teams and contribute to scientific publications
- Train and mentor junior staff members
- Maintain accurate records and documentation of all research activities
""",
                company="NovaGen Biotech Solutions",
                location="Istanbul, Turkey",
                salary="₺95,000 - ₺130,000 per month (commensurate with experience)",
                required_skills="Molecular Biology, Genetic Engineering, PCR, qPCR, Western Blot, Cell Culture, Data Analysis, Bioinformatics, GMP/GLP, Scientific Reporting"
)

        ]

        db.session.bulk_save_objects(jobs)
        db.session.commit()
        print("✅ jobs.db veritabanı başarıyla oluşturuldu ve dolduruldu.")
    else:
        print("ℹ️ jobs.db zaten dolu, yeni kayıt eklenmedi.")

