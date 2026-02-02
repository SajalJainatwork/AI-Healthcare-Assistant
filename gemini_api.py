import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("Google-API-Key"))

model = genai.GenerativeModel("gemini-1.5-pro")

def get_gemini_response(prompt_list):
    try:
        response = model.generate_content(prompt_list)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
