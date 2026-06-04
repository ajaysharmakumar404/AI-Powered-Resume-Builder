import os
from dotenv import load_dotenv
import google.generativeai as genai
from rag import retrieve_resume

# Load .env file
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Create model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def optimize_resume(resume_text, job_description):
    similar_resume = retrieve_resume(
        job_description
    )
    print("\n=== Retrieved Resume ===")
    print(similar_resume)
    print("========================\n")

    prompt = f"""
    You are an ATS and resume optimization expert.

    Candidate Resume:
    {resume_text}

    Job Description:
    {job_description}

    Retrieved Reference Resume:
    {similar_resume}
    
    Use this reference only as a style and structure guide.
    Do not copy content verbatim.

    Instructions:

    1. Improve the resume.
    2. Add ATS-friendly keywords.
    3. Improve project descriptions.
    4. Align the resume with the job description.
    5. Use the reference resume style where appropriate.
    6. Return only the optimized resume.
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"Error generating resume: {str(e)}"