from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/items")
def items():
    return jsonify(
        service="api-service",
        env=os.getenv("ENV", "dev"),
        items=[
            {"id": 1, "name": "Keyboard"},
            {"id": 2, "name": "Mouse"},
            {"id": 3, "name": "Monitor"},
        ],
    ), 200

if __name__ == "__main__":
    # Pour exécution locale (Docker utilisera gunicorn)
    app.run(host="0.0.0.0", port=3000, debug=False)
