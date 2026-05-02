import streamlit as st
from google import genai
import os
from dotenv import load_dotenv
from utils.ui import apply_ui

apply_ui()

# =========================
# 🔑 LOAD ENV (LOCAL)
# =========================
load_dotenv()

# =========================
# 🔐 GET API KEY (SECURE)
# =========================
api_key = os.getenv("GEMINI_API_KEY")

# =========================
# 🚀 GEMINI CLIENT
# =========================
client = genai.Client(api_key=api_key)

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
    placeholder="Example: Low study hours, high screen time, weak in math..."
)

# =========================
# BUTTON
# =========================
if st.button("🚀 Generate AI Advice"):

    if text.strip() == "":
        st.warning("Please enter student details!")
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
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.success("AI Insights Generated 🎯")
            st.markdown(response.text)

        except Exception as e:
            st.error("AI service failed ❌")

            st.info("""
Fallback Advice:
- Study consistently
- Reduce screen time
- Focus on weak subjects
- Maintain routine
""")