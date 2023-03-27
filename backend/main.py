from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """/ にゲットリクエストが来た時の関数

    Returns:
        _type_: _description_
    """
    return "<p>Hello, World!</p>"
