import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Health Clustering Dashboard")

# Load dataset dari repo
df = pd.read_csv("clustered_health_data.csv")

st.write("### Dataset")
st.dataframe(df)

# Pilih cluster
cluster = st.selectbox("Pilih Cluster:", sorted(df["Cluster"].unique()))

# Filter data
filtered = df[df["Cluster"] == cluster]

st.write(f"### Data untuk Cluster {cluster}")
st.dataframe(filtered)

# Plot
st.write("### Visualisasi BMI vs Activity")

plt.figure()
plt.scatter(filtered["BMI_Decile"], filtered["Activity_Decile"])
plt.xlabel("BMI Decile")
plt.ylabel("Activity Decile")
plt.title(f"Cluster {cluster}")
st.pyplot(plt)
