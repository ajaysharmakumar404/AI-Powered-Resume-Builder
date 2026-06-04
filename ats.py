import re

def calculate_ats_score(resume_text, job_description):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    keywords = set(
        re.findall(r'\b[a-zA-Z+#]+\b', job_description)
    )

    keywords = {
        word
        for word in keywords
        if len(word) > 2
    }

    matched = []
    missing = []

    for keyword in keywords:

        if keyword in resume_text:
            matched.append(keyword)
        else:
            missing.append(keyword)

    score = 0

    if len(keywords) > 0:
        score = round(
            len(matched) / len(keywords) * 100,
            2
        )

    return score, matched, missing