import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

PM1_pred = pd.read_csv("PM1_predictions.csv")

# printing the dataset to the web app
st.title("Streamlit Line Chart")

# printing the table
st.write(PM1_pred)

# creating the plotly chart
fig = px.line(PM1_pred)

# adding the heading to the streamlit web app
st.subheader("Plotly line chart in streamlit")

# creating line chart in streamlit
st.plotly_chart(fig)

# creating line chart in matplotlib
fig1, ax = plt.subplots()
ax.plot(PM1_pred)

# adding heading to streamlit line chart using matplotlib
st.subheader("Matplotlib line chart in Streamlit")

# showing the plot
st.pyplot(fig1)

# seaborn line chart in streamlit
fig2 = plt.figure(figsize=(10, 4))
sns.lineplot(PM1_pred)

# adding heading
st.subheader("Seaborn Line chart in Streamlit")

# plotting
st.pyplot(fig2)

