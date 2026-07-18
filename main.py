import os
import PyPDF2
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv


load_dotenv()



app = Flask(__name__)

# ==============================
# GEMINI CONFIGURATION
# ==============================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

# ==============================
# PDF TEXT EXTRACTION
# ==============================

def extract_text_from_pdf(file_storage):
    extracted_text = ""

    pdf_reader = PyPDF2.PdfReader(file_storage)

    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            extracted_text += page_text + "\n"

    return extracted_text


# ==============================
# SINGLE ATS ANALYSIS
# ==============================

def analyze_resume(resume_text, jd_text):

    prompt = f"""
You are an expert Applicant Tracking System (ATS).

Analyze the following Resume and Job Description.

=========================
RESUME
=========================

{resume_text}

=========================
JOB DESCRIPTION
=========================

{jd_text}

Return the output exactly in the following format.

Resume Summary

• Skills
• Experience Summary
• Education
• Tools & Technologies

Job Description Summary

• Required Skills
• Responsibilities
• Preferred Qualifications

ATS Match Analysis

• Match Percentage (0-100%)

• Matching Skills

• Missing Skills

• Candidate Strengths

• Areas for Improvement

• Resume Improvement Suggestions

Rules:

1. Use clear bullet points.
2. Do NOT use Markdown.
3. Do NOT use #.
4. Do NOT use **.
5. Keep the response professional.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    return response.text


# ==============================
# ROUTES
# ==============================

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return jsonify({"error": "Resume not uploaded"})

    file = request.files["resume"]

    jd_text = request.form.get("job_description")

    if not jd_text:
        return jsonify({"error": "Job Description is empty"})

    resume_text = extract_text_from_pdf(file)

    if resume_text.strip() == "":
        return jsonify({"error": "Unable to extract text from PDF"})

    try:

        analysis = analyze_resume(resume_text, jd_text)

        return jsonify({
            "analysis": analysis
        })

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500


# ==============================
# RUN APPLICATION
# ==============================

if __name__ == "__main__":
    app.run(debug=True)