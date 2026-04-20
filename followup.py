def detect_followup(email):
    text = (email["subject"] + " " + email["body"]).lower()

    if "waiting" in text or "no response" in text or "follow up" in text:
        return "Pending Follow-up"
    else:
        return "No Follow-up"
