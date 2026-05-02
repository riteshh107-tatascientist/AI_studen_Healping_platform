import streamlit as st
import sys
import os

# ================= PAGE CONFIG (FIRST) =================
st.set_page_config(page_title="AI Study Coach", layout="wide")

# 🔥 PATH FIX
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ================= CLEAN DARK UI (NO CONFLICT) =================
st.markdown("""
<style>

/* ===== FULL DARK BACKGROUND ===== */
.stApp {
    background: linear-gradient(135deg, #0a0f1c, #111827, #0a0f1c);
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

/* ===== BUTTON GLOW ===== */
.stButton>button {
    background: linear-gradient(45deg, #00C9A7, #007CF0);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    padding: 10px 20px;
    border: none;
    box-shadow: 0 0 15px #00C9A7;
}

.stButton>button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px #00C9A7;
}

/* ===== INPUT BOX ===== */
textarea {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# ================= IMPORT UI (AFTER FIX) =================
from utils.ui import apply_ui
apply_ui()

# ================= GEMINI =================
import google.generativeai as genai

# ================= API KEY =================
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("❌ API Key not found! Add it in Streamlit Secrets")
    st.stop()

# ================= MODEL =================
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# ================= TITLE =================
st.markdown("<h1 style='text-align:center;color:#00C9A7;'>🧠 AI Study Coach</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:white;'>Get AI-powered personalized study plan 🚀</p>", unsafe_allow_html=True)

# ================= INPUT =================
text = st.text_area(
    "Enter student details or problem",
    placeholder="Example: Study 4 hours, low attendance, weak in math, high mobile usage..."
)

# ================= BUTTON =================
if st.button("🚀 Generate AI Advice"):

    if text.strip() == "":
        st.warning("⚠️ Please enter student details!")
    else:

        prompt = f"""
You are an expert AI Student Mentor.

Return output in STRICT format:

### 📊 Weak Areas
- bullet points

### ⚠️ Problems
- short points

### 🚀 Improvement Plan
1.
2.
3.

### 📅 Daily Routine
- Morning:
- Study:
- Night:

### 💡 Motivation (1-2 lines only)

Student Data:
{text}
"""

        try:
            with st.spinner("AI is thinking... 🤖"):
                response = model.generate_content(prompt)

            st.success("✅ AI Insights Generated")

            st.markdown(f"""
            <div class="glass">
            {response.text}
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ AI service failed: {e}")

            st.info("""
Fallback Advice:
- Study consistently
- Reduce screen time
- Focus on weak subjects
- Maintain routine
""")