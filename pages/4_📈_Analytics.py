import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.set_page_config(page_title="Analytics Dashboard", layout="wide")

st.title("📊 SmartEdu AI - Advanced Analytics")

# ================= LOAD DATA =================
df = pd.read_csv("Student_Performance.csv")

# ================= METRICS =================
st.markdown("## 📈 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Total Students", len(df))
col2.metric("Avg Study Hours", round(df["study_hours"].mean(), 2))
col3.metric("Avg Attendance", round(df["attendance_percentage"].mean(), 2))

st.write("---")

# ================= PLOTLY SCATTER =================
st.markdown("## 🚀 Interactive Performance Analysis")

fig_plotly = px.scatter(
    df,
    x="study_hours",
    y="overall_score",
    color="final_grade",
    title="Study Hours vs Performance"
)

st.plotly_chart(fig_plotly, use_container_width=True)

# ================= SEABORN HEATMAP =================
st.markdown("## 🔥 Correlation Heatmap")

fig_heat, ax_heat = plt.subplots()

corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, ax=ax_heat)

st.pyplot(fig_heat)

# ================= MATPLOTLIB BAR =================
st.markdown("## 📊 Subject-wise Performance")

subjects = ["math_score", "science_score", "english_score"]
avg_scores = df[subjects].mean()

fig_bar, ax_bar = plt.subplots()
ax_bar.bar(subjects, avg_scores)

ax_bar.set_title("Average Scores")
st.pyplot(fig_bar)

# ================= HISTOGRAM =================
st.markdown("## 📉 Score Distribution")

fig_hist, ax_hist = plt.subplots()
ax_hist.hist(df["overall_score"], bins=10)

st.pyplot(fig_hist)

# ================= PIE CHART (PLOTLY) =================
st.markdown("## 🧠 Grade Distribution")

fig_pie = px.pie(
    df,
    names="final_grade",
    title="Grade Distribution"
)

st.plotly_chart(fig_pie)

# ================= INSIGHTS =================
st.markdown("## 🧠 Insights")

st.success("""
✔ More study hours → better performance  
✔ Strong correlation between subject scores  
✔ Balanced learning improves overall grade  
✔ Some students underperform due to inconsistency  
""")

# ================= FOOTER =================
st.write("---")
st.info("🚀 Multi-library analytics: Matplotlib + Seaborn + Plotly")