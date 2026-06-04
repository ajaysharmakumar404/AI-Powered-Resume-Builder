from skills import KNOWN_SKILLS


def extract_skills(text):

    text = text.lower()

    found = set()

    for category in KNOWN_SKILLS:

        for skill in KNOWN_SKILLS[category]:

            if skill.lower() in text:

                found.add(skill)

    return found


def calculate_ats_score(
        resume_text,
        job_description):

    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        job_description
    )
    print("Resume Skills:", resume_skills)
    print("JD Skills:", jd_skills)
    matched = sorted(
        resume_skills & jd_skills
    )

    missing = sorted(
        jd_skills - resume_skills
    )

    if len(jd_skills) == 0:

        score = 0

    else:

        score = round(
            len(matched)
            /
            len(jd_skills)
            * 100,
            2
        )

    return (
        score,
        matched,
        missing
    )


