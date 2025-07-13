from flask import Flask
from helix.codex_routes import codex_bp

app = Flask(__name__)
app.register_blueprint(codex_bp)

@app.route("/", methods=["GET"])
def root():
    return {"status": "Prometheus API online — Her flames reach the sky ✨"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)