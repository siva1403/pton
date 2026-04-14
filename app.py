from flask import Flask, jsonify
import os
from datetime import datetime, timezone

app = Flask(__name__)

def get_env(key):
    return os.getenv(key, "unknown")

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
        "message": "Flask app is running"
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True)