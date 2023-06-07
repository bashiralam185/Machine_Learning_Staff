import streamlit as st
import pandas as pd
import plotly.express as px

# function to open css file
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")


# reading the dataset
PM1_pred = pd.read_csv("PM1_predictions.csv")

# printing the dataset to the web app
st.title("Streamlit Buttons Tutorial")

# creating three buttons in streamlit
table = st.sidebar.button(label="Table")
line = st.sidebar.button('Line chart')
scatter = st.sidebar.button('Scattered chart')

if table:
    st.subheader('Dataset Table')
    st.table(PM1_pred)

if line :
    st.subheader("Line Chart of the Dataset")
    
    # creating the plotly chart
    fig = px.line(PM1_pred)

    # creating line chart in streamlit
    st.plotly_chart(fig)

if scatter:
    st.subheader("Scattered Chart of the Dataset")
    
    # creating the plotly chart
    fig1 = px.scatter(PM1_pred)

    # creating line chart in streamlit
    st.plotly_chart(fig1)

