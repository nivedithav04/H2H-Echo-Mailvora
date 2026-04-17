import json

def load_emails():
    with open("data/email.json", "r") as file:
        return json.load(file)

if __name__ == "__main__":
    emails = load_emails()
    print(emails)
