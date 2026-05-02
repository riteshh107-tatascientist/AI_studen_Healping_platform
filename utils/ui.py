import streamlit as st

def apply_ui():

    # ===== GLOBAL CSS =====
    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(135deg, #e0f7fa, #ffffff);
    }

    h1, h2, h3, h4, h5, h6, p, label {
        color: #1e293b !important;
    }

    .stButton>button {
        background: linear-gradient(45deg, #00C9A7, #007CF0);
        color: white;
        border-radius: 10px;
        font-weight: bold;
        padding: 10px;
    }

    /* ===== HEADER ANIMATION ===== */
    .marquee {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
    }

    .marquee span {
        display: inline-block;
        padding-left: 100%;
        animation: marquee 12s linear infinite;
        font-size: 26px;
        font-weight: bold;
        color: #00C9A7;
        text-shadow: 0 0 10px #00C9A7;
    }

    @keyframes marquee {
        0% { transform: translateX(0); }
        100% { transform: translateX(-100%); }
    }

    /* ===== FOOTER ===== */
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 8px;
        background: linear-gradient(45deg, #00C9A7, #007CF0);
        color: white;
        font-size: 14px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ===== HEADER =====
    st.markdown("""
    <div class="marquee">
    <span>🚀 AI Student Productivity System | Predict • Analyze • Improve | Hackathon Ready 🔥</span>
    </div>
    """, unsafe_allow_html=True)

    # ===== FOOTER =====
    st.markdown("""
    <div class="footer">
    🚀 AI System | Built for Hackathon | Data Science Project
    </div>
    """, unsafe_allow_html=True)