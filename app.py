from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleText": {
                    "text": str(random.randint(1, 10))
                }
            }]
        }
    }
    return jsonify(response)

@app.route('/2', methods=["GET", "POST"])
def index2():
    response = {
        "version": "2.0",
        "template": {
            "outputs": [{
                "simpleImage": {
                    "imageUrl":
                    "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                    "altText": "hello I'm Ryan"
                }
            }]
        }
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
