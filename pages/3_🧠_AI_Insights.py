import streamlit as st
import sys
import os

# ================= PAGE CONFIG =================
st.set_page_config(page_title="AI Study Coach", layout="wide")

# ================= DARK GLASS UI (FINAL FIX) =================
st.markdown("""
<style>

/* ===== DARK BACKGROUND ===== */
.stApp {
    background: radial-gradient(circle at top, #0a0f1c, #020617);
    color: white;
}

/* ===== TEXT FIX ===== */
h1, h2, h3, h4, h5, h6, p, span, label {
    color: white !important;
}

/* ===== GLASS BOX ===== */
.glass {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 15px;
    padding: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 0 20px rgba(0, 201, 167, 0.2);
    margin-top: 15px;
}

/* ===== BUTTON ===== */
.stButton>button {
    background: linear-gradient(45deg, #00C9A7, #007CF0);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    padding: 10px 20px;
    box-shadow: 0 0 15px #00C9A7;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px #007CF0;
}

/* ===== TEXT AREA ===== */
textarea {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================= GEMINI =================
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ API Key not found!")
    st.stop()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# ================= UI =================
st.markdown("<h1 style='text-align:center;color:#00C9A7;'>🧠 AI Study Coach</h1>", unsafe_allow_html=True)

text = st.text_area("Enter student details or problem")

if st.button("🚀 Generate AI Advice"):

    if text.strip() == "":
        st.warning("Enter data first!")
    else:

        prompt = f"""
You are an expert AI Student Mentor.

### 📊 Weak Areas
- bullet points

### ⚠️ Problems
- short points

### 🚀 Improvement Plan
1.
2.
3.

Student Data:
{text}
"""

        response = model.generate_content(prompt)

        st.markdown(f"""
        <div class="glass">
        {response.text}
        </div>
        """, unsafe_allow_html=True)