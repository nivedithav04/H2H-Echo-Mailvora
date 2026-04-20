from utils.classifier import classify_email
from utils.extractor import extract_action
from utils.followup import detect_followup

def process_email(email):
    category = classify_email(email)
    action = extract_action(email)
    followup = detect_followup(email)

    return {
        "category": category,
        "task": action["task"],
        "deadline": action["deadline"],
        "followup": followup
        
    }

