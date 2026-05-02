import streamlit as st
import sys
import os

# 🔥 FIX PATH FIRST (VERY IMPORTANT)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ✅ Now import works
from utils.ui import apply_ui

# Other imports
from dotenv import load_dotenv
import google.generativeai as genai

# =========================
# 🎨 APPLY UI
# =========================
apply_ui()

# =========================
# 🔐 LOAD ENV (LOCAL)
# =========================
load_dotenv()

# =========================
# 🔑 GET API KEY
# =========================
api_key = os.getenv("GEMINI_API_KEY")

# Safety check
if not api_key:
    st.error("❌ API Key not found! Add it in Streamlit Secrets or .env")
    st.stop()

# =========================
# 🚀 CONFIGURE GEMINI
# =========================
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="AI Study Coach", layout="wide")

st.title("🧠 AI Study Coach")
st.write("Get AI-powered personalized study plan 🚀")

# =========================
# INPUT
# =========================
text = st.text_area(
    "Enter student details or problem",
    placeholder="Example: Study 4 hours, low attendance, weak in math, high mobile usage..."
)

# =========================
# BUTTON
# =========================
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
            st.markdown(response.text)

        except Exception:
            st.error("❌ AI service failed")

            st.info("""
Fallback Advice:
- Study consistently
- Reduce screen time
- Focus on weak subjects
- Maintain routine
""")