from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "repository": os.getenv("GITHUB_REPOSITORY"),
        "branch": os.getenv("GITHUB_REF_NAME"),
        "commit_id": os.getenv("GITHUB_SHA"),
        "timestamp": datetime.ISTnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "message": "Flask app is running"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)