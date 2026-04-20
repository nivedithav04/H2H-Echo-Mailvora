def generate_summary(emails, classify_email, detect_followup):
    summary = {
        "total": len(emails),
        "action_required": 0,
        "meetings": 0,
        "followups": 0
    }

    for email in emails:
        category = classify_email(email)
        followup = detect_followup(email)

        if category == "Action Required":
            summary["action_required"] += 1
        elif category == "Meeting":
            summary["meetings"] += 1

        if followup == "Pending Follow-up":
            summary["followups"] += 1

    return summary
