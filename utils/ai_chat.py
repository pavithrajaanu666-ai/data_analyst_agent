import google.generativeai as genai
from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

def query_data_chat(dataframe_head, conversation_history, user_query):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
Here is a sample dataset:

{dataframe_head}

User Question:
{user_query}
"""

    response = model.generate_content(prompt)

    return response.text