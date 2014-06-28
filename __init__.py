from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

from flask.ext.mongoengine import MongoEngine

import json
import os


settings_path = 'config/settings.json'
settings = json.loads(open(settings_path, 'r').read())
db_settings = settings['db_settings']

app = Flask(__name__)  # , static_url_path='')
app.config["MONGODB_SETTINGS"] = {"DB": db_settings['DB']}
app.config["SECRET_KEY"] = db_settings["SECRET"]

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['json'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db = MongoEngine(app)

import Kadoop.views


@app.route('/')
def upload_file():
    return render_template('kadoop_form.html')
# return url_for('static', filename='kadoop_form.html')

if __name__ == '__main__':
    app.run()
