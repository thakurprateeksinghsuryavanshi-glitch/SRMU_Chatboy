"""Flask server: serves the website and the /api/chat endpoint."""
import os
from flask import Flask, jsonify, request, send_from_directory
from chatbot import get_reply

app = Flask(__name__, static_folder="static")


@app.route("/")
def home():
    return send_from_directory("static", "index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = str(data.get("message", ""))[:300]   # limit input size
    return jsonify(get_reply(message))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)
