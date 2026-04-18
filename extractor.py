import re

def extract_action(email):
    text = email["body"]

    # Simple deadline detection
    deadline = None
    if "tomorrow" in text.lower():
        deadline = "Tomorrow"
    elif "friday" in text.lower():
        deadline = "Friday"

    return {
        "task": text,
        "deadline": deadline
    }
