from flask import url_for

from Kadoop import db


class Kindle(db.Document):
    uuid = db.StringField(unique=True)
    active = db.BooleanField()


class Work(db.Document):
    data = db.ListField(db.DynamicField())
    code = db.StringField()
    done = db.BooleanField()
