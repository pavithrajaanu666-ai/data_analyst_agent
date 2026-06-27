import streamlit as st

st.set_page_config(
    page_title="AI Data Analyst Agent",
    layout="wide",
    page_icon="🤖",
    initial_sidebar_state="expanded"
)

st.sidebar.title("🧭 Navigation")
st.sidebar.markdown("Select a module below to run your pipeline.")

st.title("🤖 AI-Powered Data Analytics Platform")

st.markdown("""
Welcome to the **AI Data Analyst Agent**.

This platform helps you:

- 📂 Upload CSV/Excel datasets
- 📊 Perform automated exploratory data analysis (EDA)
- 🧹 Clean missing values and duplicates
- 📈 Generate interactive visualizations
- 🧠 Produce AI-powered business insights
- 💬 Chat with your dataset using Gemini AI

Use the **sidebar** to navigate between modules.
""")

st.info(
    "Configure your Gemini API key in the '.env' file before using the AI Insights or Chat modules."
)