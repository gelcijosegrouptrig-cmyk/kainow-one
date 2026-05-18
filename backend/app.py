from flask import Flask, request, jsonify
from flask_cors import CORS

from engine.orchestrator import Orchestrator

app = Flask(__name__)
CORS(app)

orchestrator = Orchestrator()


@app.route("/generate", methods=["POST"])
def generate():

    data = request.json

    prompt = data.get("prompt")

    result = orchestrator.execute(prompt)

    return jsonify(result)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
