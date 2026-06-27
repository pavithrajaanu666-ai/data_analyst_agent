import streamlit as st
import pandas as pd
from utils.insight_generator import generate_ai_insights
from utils.report_generator import build_pdf_report

st.title("💡 Automated AI Insights")

uploaded_file = st.file_uploader("Upload dataset to generate insights", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    data_summary = df.describe().to_string()

    if st.button("Generate AI Insights"):
        with st.spinner("Analyzing dataset with Gemini..."):
            insights = generate_ai_insights(data_summary)

            st.subheader("Key Findings")
            st.write(insights)

            if st.button("Compile & Download PDF Report"):
                pdf_path = build_pdf_report(insights)
                with open(pdf_path, "rb") as pdf_file:
                    st.download_button(
                        label="Download PDF",
                        data=pdf_file,
                        file_name="data_insights_report.pdf",
                        mime="application/pdf"
                    )