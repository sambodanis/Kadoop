from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form
from Kadoop.models import Kindle
from Kadoop import app
import json
import datetime


class WorkAPI(MethodView):

    def get(self):
        return jsonify({'res': True})

    def post(self):

        data = request.form
        print data, '2'
        return jsonify({'res': True})


app.add_url_rule('/work/', view_func=WorkAPI.as_view('work'))
# app.add_url_rule('/purchases/', view_func=PurchaseAPI.as_view('purchases'))
