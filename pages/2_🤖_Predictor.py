import streamlit as st
import joblib
import pandas as pd
import sys
import os

# ================= PAGE CONFIG (FIRST) =================
st.set_page_config(page_title="Predictor", layout="wide")

# 🔥 PATH FIX
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ================= SAFE UI (FIXED VERSION) =================
st.markdown("""
<style>

/* ===== DARK BACKGROUND FIX ===== */
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white !important;
}

/* ===== TEXT FIX ===== */
h1, h2, h3, h4, h5, h6, p, span, label {
    color: white !important;
}

/* ===== INPUT FIX ===== */
input, textarea {
    background-color: rgba(255,255,255,0.08) !important;
    color: white !important;
    border-radius: 10px;
}

/* ===== BUTTON ===== */
.stButton>button {
    background: linear-gradient(45deg, #00C9A7, #007CF0);
    color: white;
    border-radius: 10px;
    font-weight: bold;
    box-shadow: 0 0 15px #00C9A7;
}

/* ===== GLASS CARD ===== */
.glass {
    background: rgba(255,255,255,0.06);
    padding: 15px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

</style>
""", unsafe_allow_html=True)

# ================= LOAD FILES =================
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")
target_encoder = joblib.load("target_encoder.pkl")
feature_columns = joblib.load("features.pkl")

# ================= TITLE =================
st.title("🤖 Student Performance Predictor")

# ================= INPUTS =================
age = st.slider("Age", 15, 30, 18)

gender = st.selectbox("Gender", encoders["gender"].classes_)
school_type = st.selectbox("School Type", encoders["school_type"].classes_)
parent_education = st.selectbox("Parent Education", encoders["parent_education"].classes_)

study_hours = st.slider("Study Hours", 0, 12, 4)
attendance = st.slider("Attendance %", 0, 100, 75)

internet_access = st.selectbox("Internet Access", encoders["internet_access"].classes_)
travel_time = st.selectbox("Travel Time", encoders["travel_time"].classes_)
extra_activities = st.selectbox("Extra Activities", encoders["extra_activities"].classes_)
study_method = st.selectbox("Study Method", encoders["study_method"].classes_)

math = st.slider("Math Score", 0, 100, 50)
science = st.slider("Science Score", 0, 100, 50)
english = st.slider("English Score", 0, 100, 50)

overall = (math + science + english) / 3

# ================= ENCODE =================
def encode(col, value):
    return encoders[col].transform([value])[0]

# ================= INPUT =================
input_dict = {
    "age": age,
    "gender": encode("gender", gender),
    "school_type": encode("school_type", school_type),
    "parent_education": encode("parent_education", parent_education),
    "study_hours": study_hours,
    "attendance_percentage": attendance,
    "internet_access": encode("internet_access", internet_access),
    "travel_time": encode("travel_time", travel_time),
    "extra_activities": encode("extra_activities", extra_activities),
    "study_method": encode("study_method", study_method),
    "math_score": math,
    "science_score": science,
    "english_score": english,
    "overall_score": overall
}

input_df = pd.DataFrame([input_dict])

# ================= FIX FEATURE ORDER =================
input_df = input_df[feature_columns]

# ================= PREDICT =================
if st.button("🎯 Predict"):
    pred = model.predict(input_df)
    result = target_encoder.inverse_transform(pred)[0]

    st.markdown(f"""
    <div class="glass">
    📊 Predicted Grade: <b>{result}</b>
    </div>
    """, unsafe_allow_html=True)