from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello world!"


@app.route("/annotate", methods=["POST"])
def detection():
    data = request.json
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
