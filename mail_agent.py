from utils.classifier import classify_email
from utils.extractor import extract_action
from utils.followup import detect_followup
from utils.summary import generate_summary   # make sure this file exists

# 🔹 Auto reply generator
def generate_reply(category):
    if category.lower() == "meeting":
        return "I will attend the meeting. Please share the details."
    
    elif category.lower() == "finance":
        return "The payment will be processed shortly."
    
    elif category.lower() == "task":
        return "The task will be completed within the deadline."
    
    elif category.lower() == "personal":
        return "Thanks for reaching out! I will get back to you soon."
    
    else:
        return "Thank you for your email. I will review it and respond soon."


# 🔹 Main processing function
def process_email(email):
    
    # Step 1: Classification
    category = classify_email(email)
    
    # Step 2: Extract task + deadline
    action = extract_action(email)
    
    # Step 3: Follow-up detection
    followup = detect_followup(email)
    
    # Step 4: Summary generation
    summary = generate_summary(email)
    
    # Step 5: Auto reply
    reply = generate_reply(category)

    return {
        "category": category,
        "task": action.get("task", "No task found"),
        "deadline": action.get("deadline", "No deadline"),
        "followup": followup,
        "summary": summary,
        "reply": reply
    }
