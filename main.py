from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/work", methods=['GET', 'POST'])
def get_work():
    print request.data
    return {'res': True, 'work': [1, 2, 3, 4, 5, 6]}


@app.route("/complete", methods=['POST'])
def done_work():
    return {'res': True, 'msg': 'look out for potatoes'}

if __name__ == "__main__":
    app.run(port=80)
