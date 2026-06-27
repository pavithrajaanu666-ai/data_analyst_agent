import streamlit as st
import pandas as pd
from utils.cleaner import clean_data

st.title("🧹 Data Preprocessing & Cleaning")

uploaded_file = st.file_uploader("Upload dataset for cleaning", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("Missing values per column:")
    st.write(df.isnull().sum())

    impute_method = st.selectbox("Impute missing values with:", ["mean", "median", "zero"])
    drop_dupes = st.checkbox("Drop duplicate rows", value=True)

    if st.button("Run Cleaning Pipeline"):
        cleaned_df = clean_data(df, fill_method=impute_method, drop_duplicates=drop_dupes)
        st.success("Data cleaned successfully!")
        st.dataframe(cleaned_df.head())

        csv = cleaned_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Cleaned Data",
            data=csv,
            file_name='cleaned_data.csv',
            mime='text/csv',
        )