import pandas as pd
from pathlib import Path

# Resolve project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Load email logs
email_log = BASE_DIR / "logs" / "email_logs.csv"
emails = pd.read_csv(email_log)

# Define phishing indicators
suspicious_attachments = [".zip", ".html"]
suspicious_keywords = ["fake", "phish", "malicious"]

def is_phishing(row):
    sender = str(row["sender"]).lower()
    attachment = str(row["attachment"]).lower()
    link = str(row["link"]).lower()

    if any(keyword in sender for keyword in suspicious_keywords):
        return True
    if any(attachment.endswith(ext) for ext in suspicious_attachments):
        return True
    if any(keyword in link for keyword in suspicious_keywords):
        return True
    return False

# Apply detection logic
emails["phishing_flag"] = emails.apply(is_phishing, axis=1)

phishing_emails = emails[emails["phishing_flag"] == True]

print("\nPotential Phishing Emails Detected:\n")
print(phishing_emails if not phishing_emails.empty else "No phishing emails detected.")
