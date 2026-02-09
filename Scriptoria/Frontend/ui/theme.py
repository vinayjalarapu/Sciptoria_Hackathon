import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    /* Animated Gradient Background */
    .stApp {
        background: linear-gradient(
            -45deg,
            #020617,   /* deep navy */
            #0f172a,   /* slate blue */
            #1e3a8a,   /* strong blue */
            #312e81 
        );
        background-size: 400% 400%;
        animation: gradientBG 12s ease infinite;
        color: #ffffff;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Headings */
    h1, h2, h3 {
        color: #00E5FF;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: rgba(0,0,0,0.65);
        backdrop-filter: blur(10px);
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #00E5FF, #7C4DFF);
        color: white;
        border-radius: 10px;
        padding: 0.6em 1.5em;
        font-weight: 600;
        border: none;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #7C4DFF, #00E5FF);
    }

    /* Inputs */
    input, textarea {
        background-color: #121212 !important;
        color: white !important;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)
