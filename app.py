import sys
import json
import smtplib

data = json.loads(sys.argv[1])

subject = "⚠️ GitHub PR Bypass Alert"
body = f"""
User {data['user']} merged PR #{data['pr']} without required approvals.
"""

sender = "your@email.com"
receiver = "alert@email.com"

message = f"Subject: {subject}\n\n{body}"

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, "your_app_password")
    server.sendmail(sender, receiver, message)