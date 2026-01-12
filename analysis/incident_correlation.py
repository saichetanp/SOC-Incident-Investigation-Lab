import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Load logs
auth_logs = pd.read_csv(BASE_DIR / "logs" / "authentication_logs.csv")
email_logs = pd.read_csv(BASE_DIR / "logs" / "email_logs.csv")
dns_logs = pd.read_csv(BASE_DIR / "logs" / "dns_logs.csv")
endpoint_logs = pd.read_csv(BASE_DIR / "logs" / "endpoint_logs.csv")

# Identify phishing emails
phishing_emails = email_logs[
    email_logs["sender"].str.contains("fake|unknown|phish", case=False, na=False)
]

# Identify malicious DNS queries
malicious_dns = dns_logs[
    dns_logs["queried_domain"].str.contains("malicious|phish", case=False, na=False)
]

# Identify suspicious endpoint activity
endpoint_threats = endpoint_logs[
    endpoint_logs["process"].str.contains("powershell|cmd", case=False, na=False)
]

# Identify suspicious authentication
auth_threats = auth_logs[
    (auth_logs["result"] == "SUCCESS") &
    (auth_logs["location"].isin(["Russia", "China", "North Korea"]))
]

print("\n--- Incident Correlation Summary ---\n")

if not phishing_emails.empty:
    print("[+] Phishing email detected")

if not malicious_dns.empty:
    print("[+] Malicious DNS activity detected")

if not endpoint_threats.empty:
    print("[+] Suspicious endpoint execution detected")

if not auth_threats.empty:
    print("[+] Suspicious authentication detected")

# Severity assessment
signals = sum([
    not phishing_emails.empty,
    not malicious_dns.empty,
    not endpoint_threats.empty,
    not auth_threats.empty
])

severity = "Low"
if signals >= 2:
    severity = "Medium"
if signals >= 3:
    severity = "High"

print(f"\nIncident Severity: {severity}")
