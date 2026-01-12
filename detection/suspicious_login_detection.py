import pandas as pd
from pathlib import Path

# Resolve project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Build absolute path to log file
log_file = BASE_DIR / "logs" / "authentication_logs.csv"

# Read logs
logs = pd.read_csv(log_file)

# Detect suspicious logins
suspicious = logs[
    (logs["result"] == "SUCCESS") &
    (logs["location"].isin(["Russia", "China", "North Korea"]))
]

print("\nSuspicious Authentication Activity:\n")
print(suspicious if not suspicious.empty else "No suspicious activity found.")
