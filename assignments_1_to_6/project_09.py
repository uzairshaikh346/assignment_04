import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("Simple Data Dashboard")

upload_file = st.file_uploader("Choose a csv file" , type="csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summery")
    st.write(df.describe())

    st.subheader("Filter Data")
    column = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by : ", column)
    unique_value = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_value)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Selec x-axis column" ,column)
    y_column = st.selectbox("Selec y-axis column" ,column)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else: 
    st.write("Waiting for file upload")