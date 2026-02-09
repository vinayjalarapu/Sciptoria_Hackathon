import streamlit as st
from backend.main import analyze_idea
from ui.theme import apply_theme


apply_theme()

st.title("💡 Idea Vault")

idea = st.text_area("Enter your movie idea")

if st.button("Analyze Idea"):
    if idea.strip() == "":
        st.warning("Please enter an idea")
    else:
        with st.spinner("Analyzing with Groq AI..."):
            result = analyze_idea(idea)

        st.success("AI Analysis Complete")
        st.markdown(result)
