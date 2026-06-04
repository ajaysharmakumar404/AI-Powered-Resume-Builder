import re
from ats import extract_skills

def analyze_resume(resume_text):

    score = 0
    recommendations = []

    sections = {
        "education": False,
        "skills": False,
        "projects": False,
        "experience": False
    }

    text = resume_text.lower()

    for section in sections:

        if section in text:
            sections[section] = True
            score += 25

    if not sections["projects"]:
        recommendations.append(
            "Add a Projects section."
        )

    if not sections["skills"]:
        recommendations.append(
            "Add a Skills section."
        )

    if not sections["experience"]:
        recommendations.append(
            "Add Experience or Internship details."
        )

    if not sections["education"]:
        recommendations.append(
            "Add Education details."
        )

    return score, recommendations

def skill_gap(
        resume_text,
        job_description):

    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        job_description
    )

    return sorted(
        jd_skills - resume_skills
    )