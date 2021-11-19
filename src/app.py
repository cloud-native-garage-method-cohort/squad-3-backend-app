import os
from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    dd = {"msg": "hello from our app"}
    return jsonify(dd)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9010)
