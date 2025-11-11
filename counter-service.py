#!flask/bin/python
import os

from flask import Flask, request, request_started

app = Flask(__name__)
get_counter = 0
post_counter = 0


@app.route("/", methods=["GET"])
def get_index():
    global get_counter, post_counter
    get_counter += 1
    total_requests = get_counter + post_counter
    return f"""
    <h2>Counter Dashboard 📈</h2>
    <div style="background-color: #e8f5e8; padding: 15px; border-radius: 5px; margin: 10px 0;">
        <h3>📊 Request Statistics:</h3>
        <p><strong>GET requests:</strong> {get_counter}</p>
        <p><strong>POST requests:</strong> {post_counter}</p>
        <p><strong>Total requests:</strong> {total_requests}</p>
    </div>
    <p><em>Send a POST request to increment the POST counter!</em></p>
    """


@app.route("/", methods=["POST"])
def post_index():
    global post_counter
    post_counter += 1
    return "Hmm, Plus 1 please "


if __name__ == "__main__":
    # Get port from environment variable, default to 80 if not set
    port = int(os.getenv("PORT", 80))
    app.run(debug=True, port=port, host="0.0.0.0")
