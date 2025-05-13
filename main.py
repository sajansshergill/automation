import pandas as pd
from classify import classify_ticket
from router import get_assignee_email

df = pd.read_csv("data/ticket_data.csv")

df["category"] = df["description"].apply(classify_ticket)
df["assigned_to"] = df["category"].apply(get_assignee_email)

df.to_excel("classified_tickets.xlsx", index=False)
print("✔ Tickets classified and saved.")
