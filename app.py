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

# =========================
# LOAD EMAILS
# =========================
emails = load_emails()

# =========================
# SUMMARY DASHBOARD (Day 5)
# =========================
summary = generate_summary(emails, classify_email, detect_followup)

c1, c2, c3, c4 = st.columns(4)

c1.metric("📧 Total Emails", summary["total"])
c2.metric("📌 Action Required", summary["action_required"])
c3.metric("📅 Meetings", summary["meetings"])
c4.metric("🔔 Follow-ups", summary["followups"])

st.divider()

# =========================
# SEARCH & FILTER (Day 6)
# =========================
st.subheader("🔍 Search & Filter")

f1, f2 = st.columns(2)

search_query = f1.text_input("Search emails")
selected_category = f2.selectbox(
    "Filter by Category",
    ["All", "Action Required", "Meeting", "Follow-up", "Informational"]
)

st.divider()

# =========================
# EMAIL LIST (Day 4 + 5 + 6)
# =========================
if category == "Action Required":
    st.markdown(f"### 🚨 {email['subject']}")
else:
    st.markdown(f"### 📨 {email['subject']}")


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
    # EMAIL CARD UI
    # =========================
    with st.container():
        st.markdown(f"### 📨 {email['subject']}")

        col_left, col_right = st.columns([3, 1])

        # LEFT SIDE
        with col_left:
            st.write("📧 From:", email["sender"])
            st.write("📝 Message:", email["body"])
            st.write("📋 Task:", action["task"])
            st.write("⏰ Deadline:", action["deadline"])

        # RIGHT SIDE
        with col_right:
            if category == "Action Required":
                st.error(f"📌 {category}")
            elif category == "Meeting":
                st.info(f"📌 {category}")
            elif category == "Follow-up":
                st.warning(f"📌 {category}")
            else:
                st.success(f"📌 {category}")

            if followup == "Pending Follow-up":
                st.warning("🔔 Pending")
            else:
                st.success("✅ No Follow-up")

        st.divider()

