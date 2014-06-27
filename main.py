from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/work", methods=['GET', 'POST'])
def get_work():
    print request.data
    return "Hello"


@app.route("/complete", methods=['POST'])
def done_work():


if __name__ == "__main__":
    app.run()
