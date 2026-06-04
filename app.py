import streamlit as st

from parser import extract_text
from ats import calculate_ats_score
from resume_generator import optimize_resume
from analyzer import analyze_resume, skill_gap

st.set_page_config(
    page_title="AI Resume Builder",
    page_icon="📄",
    layout="wide"
)

st.title("AI Resume Builder")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    # -------------------------
    # Extract Resume Text
    # -------------------------
    text = extract_text(uploaded_file)

    # -------------------------
    # Resume Analysis
    # -------------------------
    analysis_score, recs = analyze_resume(text)

    st.subheader("Resume Health Score")

    st.metric(
        "Health Score",
        f"{analysis_score}/100"
    )

    st.subheader("Recommendations")

    if len(recs) == 0:
        st.success(
            "No major issues found."
        )
    else:
        for r in recs:
            st.write(f"- {r}")

    # -------------------------
    # Extracted Resume
    # -------------------------
    st.subheader("Extracted Text")

    st.text_area(
        "Resume Content",
        text,
        height=300
    )

    # -------------------------
    # Job Description
    # -------------------------
    job_description = st.text_area(
        "Paste Job Description"
    )

    if job_description:

        # -------------------------
        # ATS Score
        # -------------------------
        score, matched, missing = calculate_ats_score(
            text,
            job_description
        )

        st.subheader("ATS Score")

        st.metric(
            "Score",
            f"{score}%"
        )

        # -------------------------
        # Matched Skills
        # -------------------------
        st.subheader("Matched Skills")

        if matched:
            for skill in matched:
                st.write(f"✅ {skill}")
        else:
            st.write("No matching skills found.")

        # -------------------------
        # Missing Skills
        # -------------------------
        missing_skills = skill_gap(
            text,
            job_description
        )

        st.subheader("Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.write(f"❌ {skill}")
        else:
            st.success(
                "No missing skills detected."
            )

        # -------------------------
        # Generate Resume
        # -------------------------
        if st.button(
            "Generate Optimized Resume"
        ):

            with st.spinner(
                "Optimizing Resume..."
            ):

                optimized_resume = optimize_resume(
                    text,
                    job_description
                )

            st.subheader(
                "Optimized Resume"
            )

            st.text_area(
                "Generated Resume",
                optimized_resume,
                height=500
            )