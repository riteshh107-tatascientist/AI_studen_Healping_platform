import streamlit as st
from utils.ui import apply_ui
apply_ui()
# ================= PAGE CONFIG =================
st.set_page_config(page_title="AI Student System", layout="wide")

# ================= GLOBAL UI =================
st.markdown("""
<style>

/* ===== DARK BACKGROUND ===== */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
}

/* ===== TEXT ===== */
h1, h2, h3, h4, h5, h6, p, label {
    color: #e2e8f0 !important;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background: #020617;
}

/* ===== BUTTON ===== */
.stButton>button {
    background: linear-gradient(45deg, #00C9A7, #007CF0);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    padding: 10px 20px;
    border: none;
    box-shadow: 0 0 10px #00C9A7;
}
.stButton>button:hover {
    box-shadow: 0 0 20px #00C9A7, 0 0 40px #007CF0;
}

/* ===== GLOW TITLE ===== */
.glow {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #00C9A7;
    text-shadow: 
        0 0 5px #00C9A7,
        0 0 10px #00C9A7,
        0 0 20px #007CF0,
        0 0 40px #007CF0;
}

/* ===== CARD ===== */
.card {
    padding: 20px;
    border-radius: 15px;
    background: #020617;
    box-shadow: 0 0 10px #00C9A7;
    text-align: center;
    transition: 0.3s;
    color: white;
}
.card:hover {
    transform: scale(1.05);
    box-shadow: 0 0 20px #00C9A7, 0 0 40px #007CF0;
}

/* ===== HEADER MARQUEE ===== */
.marquee span {
    color: #00C9A7;
    text-shadow: 0 0 10px #00C9A7, 0 0 20px #007CF0;
}

/* ===== FOOTER ===== */
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    text-align: center;
    padding: 10px;
    background: #020617;
    color: #00C9A7;
    font-weight: bold;
    border-top: 1px solid #00C9A7;
    box-shadow: 0 -2px 10px #00C9A7;
}

</style>
""", unsafe_allow_html=True)
# ================= TITLE =================
st.markdown('<div class="glow">🎓 TIT Bhopal AI Powered Student Performance System</div>', unsafe_allow_html=True)

# ================= HERO =================
st.markdown("""
### 🔥 Transform Your Study with AI

- 🤖 Predict your academic performance  
- 🧠 Get AI-based personalized study advice  
- 📊 Analyze your strengths & weaknesses  
- 🚀 Boost productivity with smart insights  

---
""")

# ================= CARDS =================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">📊 <h3>Predictor</h3><p>Get your expected grade instantly</p></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">🧠 <h3>AI Insights</h3><p>Smart study plan using AI</p></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">📈 <h3>Analytics</h3><p>Visualize your performance</p></div>', unsafe_allow_html=True)

# ================= CTA =================
st.markdown("## 🚀 Start Now from Left Sidebar")

# ================= FOOTER =================
st.markdown("""
<div class="footer">
🚀 Built by Data Science Student | Hackathon Project | AI + ML Powered
</div>
""", unsafe_allow_html=True)