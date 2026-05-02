import streamlit as st
import pandas as pd
import streamlit as st



st.title("📊 Student Data Dashboard")

df = pd.read_csv("Student_Performance.csv")

st.metric("Total Students", len(df))
st.metric("Average Study Hours", round(df["study_hours"].mean(), 2))
st.metric("Average Attendance", round(df["attendance_percentage"].mean(), 2))

st.dataframe(df.head())

st.bar_chart(df["final_grade"].value_counts())