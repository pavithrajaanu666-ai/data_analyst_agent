import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

SYSTEM_PROMPT = """
You are an expert AI Data Analyst. Your task is to provide clear, actionable, 
and accurate business or statistical insights based on the provided data summary and user queries.
"""