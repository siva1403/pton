import sys
import json
from datetime import datetime
import os

pr_number = sys.argv[1]
user = sys.argv[2]
branch = sys.argv[3]
title = sys.argv[4]

log_file = "audit/bypass-log.jsonl"
os.makedirs("audit", exist_ok=True)

# --- Your vrules (customize here) ---
# Example rule: flag ALL merges as suspicious OR extend with API checks later
bypass_detected = True

record = {
    "pr": pr_number,
    "user": user,
    "branch": branch,
    "title": title,
    "bypass": bypass_detected,
    "time": datetime.utcnow().isoformat()
}

with open(log_file, "a") as f:
    f.write(json.dumps(record) + "\n")

print("Audit record written:", record)
