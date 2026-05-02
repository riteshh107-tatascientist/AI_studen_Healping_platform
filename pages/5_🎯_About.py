import streamlit as st

st.set_page_config(page_title="About Project", layout="wide")

# ================= GLOBAL UI =================
st.markdown("""
<style>

/* ===== BACKGROUND ===== */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* ===== TEXT ===== */
h1, h2, h3, h4, h5, h6, p {
    color: #ffffff !important;
}

/* ===== GLOW TITLE ===== */
.glow {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #00C9A7;
    text-shadow: 0 0 10px #00C9A7, 0 0 20px #007CF0, 0 0 30px #00C9A7;
}

/* ===== GLASS CARD ===== */
.card {
    padding: 25px;
    border-radius: 18px;
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(12px);
    box-shadow: 0px 6px 25px rgba(0,0,0,0.4);
    margin-bottom: 20px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.03);
    box-shadow: 0px 10px 35px rgba(0,0,0,0.6);
}

/* ===== SECTION TITLE ===== */
.section {
    font-size: 26px;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 10px;
    color: #38bdf8;
}

/* ===== FOOTER ===== */
.footer {
    text-align: center;
    padding: 12px;
    margin-top: 30px;
    background: linear-gradient(45deg, #00C9A7, #007CF0);
    color: white;
    border-radius: 10px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown('<div class="glow">🎯 SmartEdu AI - Student Productivity System</div>', unsafe_allow_html=True)

st.write("---")

# ================= PROJECT OVERVIEW =================
st.markdown('<div class="section">📌 Project Overview</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
SmartEdu AI is an advanced AI-powered student productivity system designed to analyze student behavior, predict academic performance, and provide personalized improvement strategies.<br><br>

This project integrates Machine Learning + Generative AI to not just predict results, but also guide students toward smart learning habits and real-world performance improvement.
</div>
""", unsafe_allow_html=True)

# ================= WHAT IT DOES =================
st.markdown('<div class="section">🚀 What This Project Does</div>', unsafe_allow_html=True)

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
st.markdown('<div class="section">⚙️ Technologies Used</div>', unsafe_allow_html=True)

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
st.markdown('<div class="section">🧩 How It Works</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
1️⃣ User enters student data (study hours, marks, attendance, etc.)<br><br>
2️⃣ Machine Learning model predicts performance (grade)<br><br>
3️⃣ AI analyzes behavior & generates improvement plan<br><br>
4️⃣ Dashboard shows insights, suggestions & analytics
</div>
""", unsafe_allow_html=True)

# ================= FEATURES =================
st.markdown('<div class="section">🔥 Key Features</div>', unsafe_allow_html=True)

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
st.markdown('<div class="section">🌍 Real-World Impact</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
This system can be used in schools, colleges, and ed-tech platforms to track student performance and provide personalized learning support.<br><br>

It helps students become more disciplined, focused, and productive using AI-driven insights.
</div>
""", unsafe_allow_html=True)

# ================= HACKATHON =================
st.markdown('<div class="section">🏆 Hackathon Details</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
📍 Venue: Technocrats Institute of Technology Excellence, Bhopal<br><br>
🏢 Location: AIML Department, Computer Lab - 1<br><br>
⏰ Time: 9:45 AM – 5:00 PM<br><br>
🎯 Event: MLH Hackathon 2.0<br><br>
🚀 Focus: AI Innovation, Real-world Problem Solving
</div>
""", unsafe_allow_html=True)

# ================= FOOTER =================
st.markdown("""
<div class="footer">
🚀 Built with AI + ML | Hackathon Project | SmartEdu AI System 🏆
</div>
""", unsafe_allow_html=True)