import openai

def classify_ticket(text):
    prompt = f"""
    Classify the following ticket into one category:
    ["Facilities", "IT Support", "HR", "Finance", "Sales Enablement"].

    Ticket: {text}
    Answer only the category name.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response['choices'][0]['message']['content'].strip()
