import streamlit as st
import pandas as pd
from utils.visualizer import (
    create_seaborn_distribution,
    create_plotly_scatter,
)

st.title("📈 Data Visualization Hub")

uploaded_file = st.file_uploader(
    "Upload CSV for plotting",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.dataframe(df.head())

    columns = df.columns.tolist()

    st.subheader("Distribution Plot")

    dist_col = st.selectbox("Column", columns)

    if st.button("Generate Distribution Plot"):
        fig = create_seaborn_distribution(df, dist_col)
        st.pyplot(fig)

    if len(columns) >= 2:
        st.subheader("Scatter Plot")

        x = st.selectbox("X Axis", columns)
        y = st.selectbox("Y Axis", columns, index=1)

        fig = create_plotly_scatter(df, x, y)
        st.plotly_chart(fig, use_container_width=True)