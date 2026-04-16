import json

def load_emails():
    with open("data/emails.json", "r") as file:
        data = json.load(file)
    return data
