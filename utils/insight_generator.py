import google.generativeai as genai
from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def generate_ai_insights(summary):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are a senior data analyst.

Analyze this dataset summary and provide:

1. Key Insights
2. Trends
3. Anomalies
4. Business Recommendations

Dataset Summary:

{summary}
"""

    response = model.generate_content(prompt)

    return response.text