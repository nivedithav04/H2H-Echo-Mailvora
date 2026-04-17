from utils.email_loader import load_emails
from agent.mail_agent import process_email

print("🚀 Mailvora Agent System Running...\n")

emails = load_emails()

for email in emails["emails"]:
    result = process_email(email)
    print(f"Subject: {email['subject']}")
    print(f"Result: {result}")
    print("-" * 40)
    

