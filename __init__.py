from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

from flask.ext.mongoengine import MongoEngine

import json
import os


settings_path = 'config/settings.json'
settings = json.loads(open(settings_path, 'r').read())
db_settings = settings['db_settings']

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": db_settings['DB']}
app.config["SECRET_KEY"] = db_settings["SECRET"]

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['json'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db = MongoEngine(app)

import Kadoop.views


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == '__main__':
    app.run()
