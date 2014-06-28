from flask import url_for

from Kadoop import db


class Kindle(db.Document):
    uuid = db.StringField(unique=True)
    active = db.BooleanField()


class Code(db.Document):
    code = db.StringField()


class Work(db.Document):
    data = db.ListField(db.DynamicField())
    code = db.ReferenceField(Code)
    kindle = db.ReferenceField(Kindle)
    taken = db.BooleanField()
    done = db.BooleanField()
