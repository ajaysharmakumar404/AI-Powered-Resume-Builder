import streamlit as st
from parser import extract_text

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