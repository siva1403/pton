from flask import Flask, jsonify
import os
from datetime import datetime, timezone

app = Flask(__name__)

def get_env(key):
    return os.getenv(key, "unknown")


# Example: simulate scan results (replace with real scanner output later)
def get_code_scan_results():
    return {
        "status": "completed",
        "tool": "basic-scan",
        "summary": {
            "total_files_scanned": 25,
            "issues_found": 3,
            "critical": 0,
            "high": 1,
            "medium": 1,
            "low": 1
        },
        "findings": [
            {
                "file": "app.py",
                "line": 12,
                "severity": "high",
                "issue": "Hardcoded secret detected"
            },
            {
                "file": "utils.py",
                "line": 45,
                "severity": "medium",
                "issue": "Unused import"
            }
        ]
    }


@app.route("/")
def home():
    response = {
        "status": "success",

        "service": {
            "name": "Flask App",
            "version": "1.0.0"
        },

        "repository": {
            "name": get_env("GITHUB_REPOSITORY"),
            "branch": get_env("GITHUB_REF_NAME"),
            "commit_id": get_env("GITHUB_SHA")
        },

        "runtime": {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "environment": "production"
        },

        # ✅ NEW SECTION: Code scanning results
        "code_scan": get_code_scan_results(),

        "message": "Flask app is running"
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(port=5000, debug=True)