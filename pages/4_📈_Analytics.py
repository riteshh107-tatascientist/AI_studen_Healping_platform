import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


st.title("📈 Data Analytics")

df = pd.read_csv("Student_Performance.csv")

fig, ax = plt.subplots()
ax.scatter(df["study_hours"], df["final_grade"])
ax.set_xlabel("Study Hours")
ax.set_ylabel("Final Grade")

st.pyplot(fig)