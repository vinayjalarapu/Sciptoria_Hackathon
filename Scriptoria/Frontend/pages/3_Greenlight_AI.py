import streamlit as st
from backend.main import greenlight_analysis
from ui.theme import apply_theme

apply_theme()

st.set_page_config(page_title="Greenlight AI", layout="wide")

st.title("🎬 Greenlight AI")
st.subheader("AI-powered Producer Decision Engine")

st.markdown(
    "Analyze whether your film idea is **commercially viable** before investing."
)

# Input Section
script = st.text_area(
    "📄 Paste Script / Story Summary",
    height=220,
    placeholder="Paste your screenplay or story summary here..."
)

col1, col2 = st.columns(2)

with col1:
    region = st.selectbox(
        "🌍 Target Market",
        ["India", "Global", "South India", "Hollywood"]
    )

with col2:
    budget = st.selectbox(
        "💰 Estimated Budget",
        ["Low (< ₹5 Cr)", "Medium (₹5–30 Cr)", "High (> ₹30 Cr)"]
    )

# Analyze Button
if st.button("🎯 Run Greenlight Analysis"):
    if not script.strip():
        st.warning("Please provide a script or story summary.")
    else:
        with st.spinner("Analyzing market viability..."):
            result = greenlight_analysis(script, region, budget)

        st.success("Greenlight Analysis Complete")

        st.markdown("## 📊 Producer Report")
        st.write(result)
