from flask import url_for

from Kadoop import db


class Kindle(db.Document):
    uuid = db.StringField()
    active = db.BooleanField


# class Work(db.Document):
#     kindle = db.ReferenceField(Kindle)
#     user_to = db.ReferenceField(User)
#     amount = db.FloatField()


# class Purchase(db.Document):
#     name = db.StringField(max_length=255)
#     cost = db.FloatField(min_value=0)
#     payer = db.ReferenceField(User)
#     buyins = db.ListField(db.ReferenceField(User))
#     time = db.DateTimeField()
