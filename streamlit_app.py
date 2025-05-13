import streamlit as st
import pandas as pd
from classify import classify_ticket
from router import get_assignee_email

st.title("🧠 AI Ticket Classifier")

uploaded = st.file_uploader("Upload Ticket CSV", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    df["category"] = df["description"].apply(classify_ticket)
    df["assigned_to"] = df["category"].apply(get_assignee_email)
    st.dataframe(df)
    st.download_button("Download Results", df.to_csv(index=False), "classified_tickets.csv")
