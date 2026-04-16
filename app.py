import streamlit as st
from utils.loader import load_emails

st.set_page_config(page_title="Mailvora", layout="wide")

st.title("📧🧠 Mailvora")
st.subheader("AI Email & Communication Tracker")

emails = load_emails()

st.write("## 📥 Inbox")

for email in emails:
    st.write("From:", email["sender"])
    st.write("Subject:", email["subject"])
    st.write("Message:", email["body"])
    st.write("---")
