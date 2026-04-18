def classify_email(email):
    text = (email["subject"] + " " + email["body"]).lower()

    if "deadline" in text or "complete" in text or "urgent" in text:
        return "Action Required"
    elif "meeting" in text:
        return "Meeting"
    elif "waiting" in text or "follow up" in text:
        return "Follow-up"
    else:
        return "Informational"
