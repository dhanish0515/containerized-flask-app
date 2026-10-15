from flask import Flask
import socket

app = Flask(__name__)
VERSION = "v3"

@app.route("/")
def home():
    return (
        f"<h1>Hello from my containerized app!</h1>"
        f"<p>Version: {VERSION}</p>"
        f"<p>Container ID: {socket.gethostname()}</p>"
    )

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)