from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form
from Kadoop.models import Kindle
from Kadoop import app
import json
import datetime


class WorkAPI(MethodView):

    def get(self):
        data = request.values
        for key in data:
            if key == 'id':
                uuid = data[key]
                Kindle.objects.get_or_create(uuid=uuid, active=True)
                return jsonify({'res': True, 'msg': 'Kindle Activated'})
        return jsonify({'res': False, 'msg': 'No id included'})

    def post(self):
        data = request.values
        print data
        return jsonify({'res': True})


class CodeAPI(MethodView):

    def get(self):
        return jsonify({'res': True, 'code': 'console.log(\'hello\')'})

app.add_url_rule('/work/', view_func=WorkAPI.as_view('work'))
app.add_url_rule('/code/', view_func=CodeAPI.as_view('code'))
# app.add_url_rule('/purchases/', view_func=PurchaseAPI.as_view('purchases'))
