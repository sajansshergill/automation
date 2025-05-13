import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_ticket(text):
    prompt = f"""
Classify the following ticket into one category:
["Facilities", "IT Support", "HR", "Finance", "Sales Enablement"].

Ticket: {text}

Only respond with the category name.
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"
