from flask import Flask, jsonify, request

app = Flask(__name__)

def kakao_simple_text(text):
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {"simpleText": {"text": text}}
            ]
        }
    }

@app.route("/", methods=["GET"])
def home():
    return "OK"

@app.route("/skill", methods=["POST"])
def skill():
    body = request.get_json(silent=True) or {}
    utterance = body.get("userRequest", {}).get("utterance", "")

    return jsonify(kakao_simple_text(f"사용자 입력: {utterance}"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
