import streamlit as st

st.set_page_config(page_title="About Project", layout="wide")

# ================= HEADER =================
st.markdown("""
<style>
.glow {
    font-size: 38px;
    font-weight: bold;
    text-align: center;
    color: #00C9A7;
    text-shadow: 0 0 10px #00C9A7, 0 0 20px #007CF0;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background: #ffffff;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="glow">🎯 SmartEdu AI - Student Productivity System</div>', unsafe_allow_html=True)

st.write("---")

# ================= PROJECT OVERVIEW =================
st.markdown("## 📌 Project Overview")

st.markdown("""
<div class="card">
SmartEdu AI is an advanced AI-powered student productivity system designed to analyze student behavior, predict academic performance, and provide personalized improvement strategies.

This project combines Machine Learning with Generative AI to not only predict outcomes but also guide students toward better learning habits.
</div>
""", unsafe_allow_html=True)

# ================= WHAT IT DOES =================
st.markdown("## 🚀 What This Project Does")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    📊 Predict student performance using ML model<br><br>
    🧠 Generate AI-based personalized study plans<br><br>
    📈 Analyze strengths & weaknesses<br><br>
    ⚡ Improve productivity with smart insights
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    🎯 Helps students focus on weak areas<br><br>
    📅 Suggests daily study routine<br><br>
    📉 Reduces distractions & improves consistency<br><br>
    🚀 Boosts academic performance
    </div>
    """, unsafe_allow_html=True)

# ================= TECHNOLOGY =================
st.markdown("## ⚙️ Technologies Used")

st.markdown("""
<div class="card">
✔ Python (Core Programming)<br>
✔ Pandas & NumPy (Data Processing)<br>
✔ Scikit-learn (Machine Learning Model)<br>
✔ Streamlit (Interactive Dashboard)<br>
✔ Google Gemini API (AI Insights)<br>
</div>
""", unsafe_allow_html=True)

# ================= HOW IT WORKS =================
st.markdown("## 🧩 How It Works")

st.markdown("""
<div class="card">
1️⃣ User enters student details (study hours, marks, attendance, etc.)<br><br>
2️⃣ Machine Learning model predicts performance (grade)<br><br>
3️⃣ Gemini AI analyzes behavior and generates improvement plan<br><br>
4️⃣ Dashboard shows insights, suggestions, and analytics<br>
</div>
""", unsafe_allow_html=True)

# ================= FEATURES =================
st.markdown("## 🔥 Key Features")

st.markdown("""
<div class="card">
✨ AI Study Coach (Personalized Advice)<br>
✨ Performance Prediction System<br>
✨ Interactive Dashboard UI<br>
✨ Real-time Input Analysis<br>
✨ Secure API Integration<br>
✨ Clean & Professional Design<br>
</div>
""", unsafe_allow_html=True)

# ================= IMPACT =================
st.markdown("## 🌍 Real-World Impact")

st.markdown("""
<div class="card">
This system can be used in schools, colleges, and ed-tech platforms to track student performance and provide personalized learning support.

It helps students become more disciplined, focused, and productive using AI.
</div>
""", unsafe_allow_html=True)

# ================= HACKATHON INFO =================
st.markdown("## 🏆 Hackathon Details")

st.markdown("""
<div class="card">
📍 Venue: Technocrats Institute of Technology Excellence, Bhopal<br><br>
🏢 Location: AIML Department, Computer Lab - 1<br><br>
⏰ Time: 9:45 AM – 5:00 PM<br><br>
🎯 Event: MLH Hackathon 2.0<br><br>
📢 Organized for innovation, AI solutions, and real-world problem solving
</div>
""", unsafe_allow_html=True)

# ================= FOOTER =================
st.write("---")
st.success("🚀 Built with AI + ML for Hackathon | SmartEdu AI System 🏆")