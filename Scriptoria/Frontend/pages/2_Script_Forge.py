import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import io
from ui.theme import apply_theme
from backend.main import (
    generate_story_structure,
    generate_scenes,
    generate_dialogue
)

apply_theme()

def generate_pdf(content):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    for line in content.split("\n"):
        story.append(Paragraph(line.replace("&", "&amp;"), styles["Normal"]))

    doc.build(story)
    buffer.seek(0)
    return buffer

st.set_page_config(page_title="ScriptForge", layout="wide")

st.title("📝 ScriptForge")
st.subheader("AI Screenwriting Studio")

st.markdown(
    "Turn your idea into a **structured screenplay** step-by-step."
)

# ===============================
# Input Section
# ===============================

idea = st.text_area(
    "💡 Film Idea",
    height=150,
    placeholder="Enter your film idea here..."
)

col1, col2 = st.columns(2)

with col1:
    genre = st.selectbox(
        "🎭 Genre",
        ["Drama", "Thriller", "Sci-Fi", "Romance", "Action", "Comedy"]
    )

with col2:
    tone = st.selectbox(
        "🎨 Tone",
        ["Dark", "Emotional", "Light-hearted", "Suspenseful", "Inspirational"]
    )

# ===============================
# Story Structure
# ===============================

if st.button("🧱 Generate Story Structure"):
    if not idea.strip():
        st.warning("Please enter a film idea.")
    else:
        with st.spinner("Creating story structure..."):
            story_structure = generate_story_structure(idea, genre, tone)

        st.session_state["story_structure"] = story_structure

        st.success("Story Structure Generated")
        st.markdown("### 📐 Story Structure")
        st.write(story_structure)

# ===============================
# Scene Generation
# ===============================

if "story_structure" in st.session_state:
    if st.button("🎬 Generate Scenes"):
        with st.spinner("Expanding into scenes..."):
            scenes = generate_scenes(st.session_state["story_structure"])

        st.session_state["scenes"] = scenes

        st.success("Scenes Generated")
        st.markdown("### 🎞️ Scene Breakdown")
        st.write(scenes)

# ===============================
# Dialogue Generation
# ===============================

if "scenes" in st.session_state:
    scene_input = st.text_area(
        "🎙️ Paste ONE Scene to Generate Dialogues",
        height=150,
        placeholder="Paste a single scene here..."
    )

    if st.button("🗣️ Generate Dialogue"):
        if not scene_input.strip():
            st.warning("Please paste a scene.")
        else:
            with st.spinner("Writing cinematic dialogues..."):
                dialogue = generate_dialogue(scene_input)

            st.success("Dialogue Generated")
            st.markdown("### 🎭 Screenplay Scene")
            st.write(dialogue)

# ===============================
# PDF Export
# ===============================

if "story_structure" in st.session_state:
    full_script = st.session_state.get("story_structure", "")

    if "scenes" in st.session_state:
        full_script += "\n\nSCENES\n\n" + st.session_state["scenes"]

    st.markdown("## 📄 Export Script")

    pdf_buffer = generate_pdf(full_script)

    st.download_button(
        label="📥 Download Script as PDF",
        data=pdf_buffer,
        file_name="ScriptForge_Screenplay.pdf",
        mime="application/pdf"
    )
