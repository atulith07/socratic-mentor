import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_KEY"))
model = genai.GenerativeModel('gemini-2.5-pro')

def socratic_probe(topic: str) -> str:
    prompt = f"""
    You are Socrates. For '{topic}', generate exactly 3 deep probing questions.
    NEVER explain or give facts. Number them 1-3.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

if __name__ == "__main__":
    print(socratic_probe("photosynthesis"))
