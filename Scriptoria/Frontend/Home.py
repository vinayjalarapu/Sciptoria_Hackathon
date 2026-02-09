import streamlit as st

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Scriptoria",
    page_icon="🎬",
    layout="wide"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>

/* ===== Animated Gradient Background ===== */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        -45deg,
        #020617,   /* deep navy */
        #0f172a,   /* slate blue */
        #1e3a8a,   /* strong blue */
        #312e81 
    );
    background-size: 400% 400%;
    animation: gradientBG 20s ease infinite;
}

/* Gradient animation */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Main container spacing */
.block-container {
    padding-top: 3rem;
}

/* ===== Hero Text ===== */
.hero-title {
    font-size: 3rem;
    font-weight: 700;
    letter-spacing: 1px;
}

.hero-subtitle {
    font-size: 1.2rem;
    color: #c7d2fe;
    margin-top: -10px;
}

/* ===== Glass Cards ===== */
.card {
    background: rgba(22, 27, 34, 0.85);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 18px;
    padding: 2rem;
    border: 1px solid rgba(255,255,255,0.08);
    height: 100%;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(0,0,0,0.35);
}

/* Feature text */
.feature-title {
    font-size: 1.1rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}

.feature-text {
    color: #e5e7eb;
    font-size: 0.95rem;
}

/* ===== Sidebar Glass ===== */
section[data-testid="stSidebar"] {
    background: rgba(10, 15, 25, 0.9);
    backdrop-filter: blur(16px);
}

/* ===== Footer ===== */
.footer {
    text-align: center;
    color: #9ca3af;
    margin-top: 3rem;
    font-size: 0.9rem;
}

</style>
""", unsafe_allow_html=True)


# ------------------ HERO SECTION ------------------
st.markdown("<div class='hero-title'>🎬 Scriptoria</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='hero-subtitle'>Generative AI Powered Film Pre-Production System</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------ FEATURE CARDS ------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
        <div class="feature-title">💡 Idea Intelligence</div>
        <div class="feature-text">
            Analyze and refine raw film ideas using AI-driven insights and structured feedback.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="feature-title">✍️ Script Generation</div>
        <div class="feature-text">
            Transform concepts into structured screenplay drafts with coherent narrative flow.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="feature-title">🚦 Greenlight Scoring</div>
        <div class="feature-text">
            Evaluate commercial, creative, and audience potential before production decisions.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
        <div class="feature-title">🎨 Visual Planning</div>
        <div class="feature-text">
            Assist in defining cinematic tone, visual style, and thematic direction.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ------------------ CTA SECTION ------------------
st.markdown("<br><br>", unsafe_allow_html=True)

st.success("Select a module from the sidebar to begin your creative workflow 🚀")

# ------------------ FOOTER ------------------
st.markdown("""
<div class="footer">
    Built for rapid ideation • Designed for creators • Powered by AI
</div>
""", unsafe_allow_html=True)
