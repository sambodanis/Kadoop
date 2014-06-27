from flask import Flask
import os

app = Flask(__name__)


@app.route('/', methods=['POST'])
def pull():
    os.system('git pull')

    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
