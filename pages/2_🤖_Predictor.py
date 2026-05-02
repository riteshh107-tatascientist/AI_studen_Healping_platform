import streamlit as st
import joblib
import pandas as pd
import streamlit as st
from utils.ui import apply_ui
apply_ui()
# Load files
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")
target_encoder = joblib.load("target_encoder.pkl")
feature_columns = joblib.load("features.pkl")

st.title("🤖 Student Performance Predictor")

# Inputs
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

# Encode function
def encode(col, value):
    return encoders[col].transform([value])[0]

# Create input
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

# Match training feature order
input_df = input_df[feature_columns]

# Prediction
if st.button("🎯 Predict"):
    pred = model.predict(input_df)
    result = target_encoder.inverse_transform(pred)[0]

    st.success(f"📊 Predicted Grade: {result}")