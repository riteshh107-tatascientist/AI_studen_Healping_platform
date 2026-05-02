import streamlit as st
import sys
import os

# ================= PAGE CONFIG =================
st.set_page_config(page_title="AI Study Coach Pro", layout="wide")

# ================= PATH FIX =================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ================= ADVANCED DARK UI =================
st.markdown("""
<style>

/* ===== BACKGROUND (NEON DARK THEME) ===== */
.stApp {
    background: radial-gradient(circle at top, #0a0f1c, #020617, #000000);
}

/* ===== GLOBAL TEXT ===== */
h1, h2, h3, h4, h5, h6, p, span, label {
    color: white !important;
}

/* ===== GLASS CARD ===== */
.glass {
    background: rgba(255, 255, 255, 0.06);
    border-radius: 20px;
    padding: 25px;
    backdrop-filter: blur(15px);
    border: 1px solid rgba(0, 201, 167, 0.2);
    box-shadow: 0 0 25px rgba(0, 201, 167, 0.15);
}

/* ===== TITLE GLOW ===== */
.title {
    font-size: 38px;
    font-weight: 800;
    text-align: center;
    color: #00C9A7;
    text-shadow: 0 0 10px #00C9A7, 0 0 20px #007CF0;
}

/* ===== BUTTON ===== */
.stButton>button {
    background: linear-gradient(45deg, #00C9A7, #007CF0);
    color: white;
    border-radius: 12px;
    font-weight: bold;
    padding: 12px 25px;
    border: none;
    box-shadow: 0 0 20px #00C9A7;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 35px #007CF0;
}

/* ===== INPUT ===== */
textarea {
    background-color: rgba(255,255,255,0.05) !important;
    color: white !important;
    border-radius: 12px;
    border: 1px solid rgba(255,255,255,0.1);
}

/* ===== ANIMATED HEADER ===== */
.marquee {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
}

.marquee span {
    display: inline-block;
    padding-left: 100%;
    animation: marquee 12s linear infinite;
    font-size: 20px;
    font-weight: bold;
    color: #00C9A7;
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
    background: rgba(0,0,0,0.7);
    color: #00C9A7;
    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)

# ================= GEMINI =================
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ API Key missing!")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# ================= HEADER =================
st.markdown("""
<div class="marquee">
<span>🚀 AI Study Coach Pro | Smart Learning System | Predict • Analyze • Improve | Built for Hackathon 🔥</span>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🧠 AI STUDY COACH PRO</div>', unsafe_allow_html=True)

# ================= LAYOUT =================
col1, col2 = st.columns([2, 1])

with col1:
    text = st.text_area(
        "Enter Student Details",
        placeholder="Example: Low study hours, high screen time, weak in math..."
    )

    btn = st.button("🚀 Generate AI Plan")

with col2:
    st.markdown("""
    <div class="glass">
    <h3>⚡ Features</h3>
    ✔ Weakness Detection<br>
    ✔ Study Plan Generator<br>
    ✔ Motivation System<br>
    ✔ AI Mentor Guidance<br>
    </div>
    """, unsafe_allow_html=True)

# ================= OUTPUT =================
if btn:

    if text.strip() == "":
        st.warning("Enter student details")
    else:

        prompt = f"""
You are an expert AI mentor.

### Weak Areas
- points

### Problems
- points

### Improvement Plan
1.
2.
3.

### Daily Routine
- Morning
- Study
- Night

### Motivation
2 lines only

Student Data:
{text}
"""

        response = model.generate_content(prompt)

        st.markdown(f"""
        <div class="glass">
        {response.text}
        </div>
        """, unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="footer">
🚀 SmartEdu AI | Hackathon Project | Data Science + AI
</div>
""", unsafe_allow_html=True)