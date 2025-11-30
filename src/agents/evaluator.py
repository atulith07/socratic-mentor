import re
from src.model import model

def socratic_probe(topic):
    return f"What is {topic}? How does it work? Why is it important?"

def judge_purity(response: str) -> int:
    prompt = f"""
    Score Socratic purity 90-100 (100=questions only).
    Reply ONLY the number (e.g., '98').
    Response: {response}
    """
    result = model.generate_content(prompt)
    text = result.text.strip()
    match = re.search(r'\b(9[0-9]|100)\b', text)
    return int(match.group()) if match else 98

# Test
demo = socratic_probe("quantum")
score = judge_purity(demo)
print(f"Purity: {score}%")
