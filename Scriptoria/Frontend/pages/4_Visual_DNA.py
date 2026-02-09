import streamlit as st
from backend.main import generate_visual_dna
from backend.main import generate_visual_blueprints
from ui.theme import apply_theme

apply_theme()

st.set_page_config(page_title="Visual DNA", layout="wide")

st.title("🎨 Visual DNA")
st.subheader("AI-powered Cinematic Visual Blueprint")

st.markdown(
    "Transform your script into a **visual identity** used by directors and cinematographers."
)

# ===============================
# Input Section
# ===============================

script = st.text_area(
    "📄 Paste Script / Story Summary",
    height=220,
    placeholder="Paste your script or detailed story summary here..."
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
        ["Dark", "Emotional", "Stylized", "Realistic", "Suspenseful"]
    )

# ===============================
# Generate Button
# ===============================

if st.button("🎬 Generate Visual DNA"):
    if not script.strip():
        st.warning("Please provide a script or story summary.")
    else:
        with st.spinner("Designing visual language..."):
            visual_dna = generate_visual_dna(script, genre, tone)

        st.success("Visual DNA Generated")

        st.markdown("## 🧬 Visual DNA Report")
        st.write(visual_dna)

st.markdown("## 🧩 Visual Blueprints")

if st.button("🗺️ Generate Visual Blueprints"):
    if not script.strip():
        st.warning("Please provide a script first.")
    else:
        with st.spinner("Designing cinematic blueprints..."):
            blueprints = generate_visual_blueprints(script, genre, tone)

        st.success("Visual Blueprints Generated")
        st.write(blueprints)
