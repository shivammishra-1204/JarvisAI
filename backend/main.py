
from flask import Flask, jsonify, send_from_directory
import os

from voice_engine import takeCommand, execute_command

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="")


@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/status")
def status():
    return jsonify({
        "listening": False,
        "status": "System Ready",
        "assistant": "JARVIS"
    })


@app.route("/command", methods=["POST"])
def command():
    try:
        print("JARVIS is activating microphone...")

        query = takeCommand()

        if not query:
            return jsonify({
                "success": False,
                "command": "",
                "response": "Sorry, I couldn't understand that."
            })

        response = execute_command(query)

        return jsonify({
            "success": True,
            "command": query,
            "response": response
        })

    except Exception as error:
        print("ERROR:", error)

        return jsonify({
            "success": False,
            "command": "",
            "response": "Something went wrong with the voice system."
        }), 500


if __name__ == "__main__":
    print("JARVIS SERVER STARTING...")
    app.run(host="127.0.0.1", port=5000, debug=False)
