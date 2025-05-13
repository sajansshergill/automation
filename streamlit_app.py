import streamlit as st
import pandas as pd
from classify import classify_ticket
from router import get_assignee_email

st.set_page_config(page_title="AI Ticket Classifier", page_icon="🤖")

st.title("🧠 AI-Powered Ticket Classifier")
st.markdown("Upload a CSV file with at least a **`description`** column. The AI will classify the ticket and assign it to a department.")

uploaded_file = st.file_uploader("📁 Upload Ticket CSV", type="csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("✅ File uploaded. Columns found:", df.columns.tolist())

        if "description" not in df.columns:
            st.error("❌ Your CSV must include a 'description' column. Please fix and re-upload.")
        else:
            with st.spinner("⏳ Classifying tickets using GPT-4..."):
                df["category"] = df["description"].apply(classify_ticket)
                df["assigned_to"] = df["category"].apply(get_assignee_email)

            st.success("🎉 Classification complete!")
            st.dataframe(df)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name="classified_tickets.csv",
                mime="text/csv"
            )

    except Exception as e:
        st.error(f"⚠️ Error reading the file: {e}")
