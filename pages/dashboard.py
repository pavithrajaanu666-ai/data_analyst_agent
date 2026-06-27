import streamlit as st
import pandas as pd
from utils.analyzer import get_summary_statistics

st.title("📊 Analysis Dashboard")

uploaded_file = st.sidebar.file_uploader("Upload Raw Dataset (CSV)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("Dataset loaded successfully!")

    st.subheader("Raw Data Preview")
    st.dataframe(df.head())

    st.subheader("Descriptive Statistics Summary")
    stats = get_summary_statistics(df)
    st.json(stats)
else:
    st.info("Upload a CSV file from the sidebar to begin analysis.")