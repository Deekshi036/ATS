# 📄 ATS Resume Analyzer

An AI-powered **Applicant Tracking System (ATS) Resume Analyzer** built using **Python, Flask, and Google Gemini AI**. The application analyzes a candidate's resume against a job description and provides an ATS match score along with detailed insights and improvement suggestions.

---

## 🚀 Features

- Upload Resume in PDF format
- Extract text from PDF resumes
- AI-powered Resume Parsing
- Job Description Analysis
- ATS Match Percentage
- Matching Skills Detection
- Missing Skills Identification
- Resume Strengths Analysis
- Personalized Improvement Suggestions
- User-friendly Web Interface

---

## 🛠️ Tech Stack

- Python
- Flask
- Google Gemini API
- PyPDF2
- HTML
- CSS
- JavaScript
- Gunicorn
- Render

---

## 📂 Project Structure

```
ATS/
│── templates/
│   └── index.html
│
│── uploads/
│
│── main.py
│── requirements.txt
│── runtime.txt
│── Procfile
│── .gitignore
│── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ATS.git
cd ATS
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file and add:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run the Application

```bash
python main.py
```

Open your browser and visit:

```
http://127.0.0.1:8080
```

---

## 🌐 Live Demo

**Live Application:**  
https://ats-gjq7.onrender.com

---

## 📊 How It Works

1. Upload a Resume (PDF)
2. Enter the Job Description
3. Resume text is extracted using PyPDF2
4. Google Gemini AI parses the resume
5. Job description is analyzed
6. ATS match score is calculated
7. Matching skills, missing skills, strengths, and improvement suggestions are displayed

---

## 📌 Future Enhancements

- DOCX Resume Support
- Download Analysis Report as PDF
- Multiple Resume Comparison
- Resume Keyword Highlighting
- User Authentication
- Dashboard Analytics

---

## 👩‍💻 Author

**Sai Deekshitha**

GitHub: https://github.com/Deekshi036

---

## ⭐ If you found this project useful, don't forget to Star ⭐ the repository.
