import streamlit as st
from utils.loader import load_emails
from utils.classifier import classify_email
from utils.extractor import extract_action
from utils.followup import detect_followup
from utils.summary import generate_summary

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Mailvora", layout="wide")

# =========================
# HEADER
# =========================
st.title("📧 Mailvora")
st.caption("Smart Email Intelligence Dashboard")

# Load emails
emails = load_emails()

# =========================
# SUMMARY DASHBOARD
# =========================
summary = generate_summary(emails, classify_email, detect_followup)

col1, col2, col3, col4 = st.columns(4)

col1.metric("📧 Total Emails", summary["total"])
col2.metric("📌 Action Required", summary["action_required"])
col3.metric("📅 Meetings", summary["meetings"])
col4.metric("🔔 Follow-ups", summary["followups"])

st.divider()

# =========================
# SEARCH & FILTER
# =========================
st.subheader("🔍 Search & Filter")

col1, col2 = st.columns(2)

search_query = col1.text_input("Search emails")
selected_category = col2.selectbox(
    "Filter by Category",
    ["All", "Action Required", "Meeting", "Follow-up", "Informational"]
)

st.divider()

# =========================
# EMAIL LIST
# =========================
st.subheader("📥 Inbox")

for email in emails:
    category = classify_email(email)
    action = extract_action(email)
    followup = detect_followup(email)

    # 🔍 SEARCH FILTER
    if search_query:
        if search_query.lower() not in (email["subject"] + email["body"]).lower():
            continue

    # 🎯 CATEGORY FILTER
    if selected_category != "All" and category != selected_category:
        continue

    # =========================
    # EMAIL CARD
    # =========================
    with st.container():
        st.markdown(f"### 📨 {email['subject']}")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write("📧 From:", email["sender"])
            st.write("📝 Message:", email["body"])
            st.write("📋 Task:", action["task"])
            st.write("⏰ Deadline:", action["deadline"])

        with col2:
            # Category badge
            if category == "Action Required":
                st.error(f"📌 {category}")
            elif category == "Meeting":
                st.info(f"📌 {category}")
            elif category == "Follow-up":
                st.warning(f"📌 {category}")
            else:
                st.success(f"📌 {category}")

            # Follow-up status
            if followup == "Pending Follow-up":
                st.warning("🔔 Pending")
            else:
                st.success("✅ No Follow-up")

        st.divider()
