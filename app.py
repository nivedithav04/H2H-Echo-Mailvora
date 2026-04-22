import streamlit as st
from utils.loader import load_emails
from mail_agent import process_email

st.set_page_config(page_title="Mailvora", layout="wide")

st.title("📧 Mailvora")
st.caption("Smart Email Intelligence Dashboard")

emails = load_emails()

processed_emails = []

for email in emails:
    result = process_email(email)
    processed_emails.append({**email, **result})

total = len(processed_emails)
action_required = sum(1 for e in processed_emails if e["category"] == "Action Required")
meetings = sum(1 for e in processed_emails if e["category"] == "Meeting")
followups = sum(1 for e in processed_emails if e["followup"] == "Pending Follow-up")

c1, c2, c3, c4 = st.columns(4)

c1.metric("📧 Total Emails", total)
c2.metric("📌 Action Required", action_required)
c3.metric("📅 Meetings", meetings)
c4.metric("🔔 Follow-ups", followups)

st.divider()

st.subheader("🔍 Search & Filter")

f1, f2 = st.columns(2)

search_query = f1.text_input("Search emails")

selected_category = f2.selectbox(
    "Filter by Category",
    ["All", "Action Required", "Meeting", "Follow-up", "Informational"]
)

st.divider()

for email in processed_emails:

    if search_query:
        if search_query.lower() not in (email["subject"] + email["body"]).lower():
            continue

    if selected_category != "All" and email["category"] != selected_category:
        continue

    with st.container():

        if email["category"] == "Action Required":
            st.markdown(f"### 🚨 {email['subject']}")
        else:
            st.markdown(f"### 📨 {email['subject']}")

        col_left, col_right = st.columns([3, 1])

        with col_left:
            st.write("📧 From:", email.get("sender", "Unknown"))
            st.write("📝 Message:", email["body"])
            st.write("📋 Task:", email["task"])
            st.write("⏰ Deadline:", email["deadline"])
            st.write("🧠 Summary:", email["summary"])
            st.write("💬 Reply:", email["reply"])

        with col_right:
            if email["category"] == "Action Required":
                st.error(f"📌 {email['category']}")
            elif email["category"] == "Meeting":
                st.info(f"📌 {email['category']}")
            elif email["category"] == "Follow-up":
                st.warning(f"📌 {email['category']}")
            else:
                st.success(f"📌 {email['category']}")

            if email["followup"] == "Pending Follow-up":
                st.warning("🔔 Pending")
            else:
                st.success("✅ No Follow-up")

        st.d


