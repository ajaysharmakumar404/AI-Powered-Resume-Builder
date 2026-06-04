import streamlit as st
from parser import extract_text
from ats import calculate_ats_score

st.title("AI Resume Builder")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    st.subheader("Extracted Text")

    st.text_area(
        "Resume Content",
        text,
        height=300
    )

    # ATS Section
    job_description = st.text_area(
        "Paste Job Description"
    )

    if job_description:
        score, matched, missing = calculate_ats_score(
            text,
            job_description
        )

        st.subheader("ATS Score")

        st.metric(
            "Score",
            f"{score}%"
        )

        st.subheader("Matched Skills")

        st.write(matched)

        st.subheader("Missing Skills")

        st.write(missing)