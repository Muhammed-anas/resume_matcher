🚀 Resume Matcher — AI-Powered Resume vs Job Description Analyzer

Resume Matcher is an AI-driven application that compares a candidate’s resume text with a job description and generates a match score, list of missing skills, and a concise summary.
It helps job seekers understand their skill gaps and assists companies in evaluating candidates more efficiently.

🧠 Features

✔ Compare resume text and job descriptions

✔ Generate match score (0–100%)

✔ Detect missing or weak skills

✔ AI-generated summary of the comparison

✔ Local, privacy-friendly AI powered by Ollama

✔ Clean input UI using Django Forms + Crispy Forms

🛠 Tech Stack
Backend

Django

Django Forms

Crispy Forms

Frontend

HTML

CSS

AI

Ollama (local LLM runtime)

Model: llama3.2

Environment

UV (faster alternative to pip for syncing Python packages)

⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/resume-matcher.git
cd resume-matcher

2. Sync all dependencies
uv sync

3. Run the Django backend
cd backend
python manage.py runserver


Backend server will be available at:
👉 http://127.0.0.1:8000/

4. Start the Ollama AI server

Make sure Ollama is installed and running:

AI API server:
👉 http://localhost:11434/api/generate

🧪 Example Input & Output
Input

Resume Text:

“Experienced Python developer with Django and REST API skills.”

Job Description:

“Looking for a Python developer with experience in Django, REST APIs, and React.”

Output
{
  "match_score": 82,
  "missing_skills": ["React"],
  "summary": "Candidate matches core Python, Django, and API skills but lacks React experience."
}

🧠 Why Ollama + Llama 3.2?

Runs LLMs locally

100% private (no data leaves your machine)

Lightweight and ideal for low–medium RAM systems

Easy to integrate with Django

Fast inference for text-based tasks

🔄 Alternative Approach

A more advanced version of this project could:

Use Django REST Framework

Integrate APIs from:

LinkedIn

Indeed

Naukri

Glassdoor

This would enable automatic extraction of real job descriptions and real-time resume matching.

⚠️ Limitations

Using the lightweight llama3.2 model introduces some constraints:

May produce inconsistent or inaccurate answers

Limited reasoning capabilities

Can struggle with tool-calling or complex queries

Not suitable for enterprise-scale workloads

For better performance, upgrade to:

Gemma 2 (Google)

GPT-4 / GPT-4o (OpenAI)

Llama 3.1 (70B)

🚀 Future Enhancements
🔧 1. Stronger AI Model

Upgrade to larger or cloud-based LLMs for better accuracy.

🎨 2. Modern Frontend

Rebuild UI using:

React

Tailwind CSS

Next.js

🔐 3. Authentication System

Add:

Login

Signup

Saved history of comparisons

Resume upload (PDF → text extraction)

🏢 4. Employer Dashboard

Upload job descriptions

Auto-screen multiple resumes

Filter candidates based on match score

🌍 5. Deployment

Deploy to:

Render

Railway

DigitalOcean

Docker containers

🏁 Conclusion

Resume Matcher helps both job seekers and HR teams:

Understand skill gaps

Speed up initial screening

Improve hiring accuracy

Save time by automating comparison

This project demonstrates practical use of AI, Django, and local LLMs to solve real-world problems.

⭐ Like this project?

If you find it useful, consider giving it a star ⭐ on GitHub!
