from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form

from Kadoop.models import Kindle, Work
from Kadoop import app

import json
import datetime


class WorkAPI(MethodView):

    def get(self):
        data = request.values
        # print data
        num_devices = Kindle.objects()
        print len(num_devices)
        return jsonify({'res': True})

    def post(self):
        data = request.values
        for key in data:
            if key == 'id':
                uuid = data[key]
                kindle = Kindle.objects.get_or_create(
                    uuid=uuid)[0]
                kindle.active = True
                print 'Kindle with id %s added' % kindle.uuid
                kindle.save()
                return jsonify({'res': True, 'msg': 'Kindle Activated'})
        return jsonify({'res': False, 'msg': 'No id included'})


class CodeAPI(MethodView):

    def get(self):
        return jsonify({'res': True, 'code': 'function(args) {return args * args}', 'data': [5, 6]})

    def post(self):
        try:
            data = request.files
            print data
            data = data['data'].read()
            data = json.loads(data)
        except Exception, e:
            return jsonify({'res': False, 'msg': 'No data or code included'})

        # if 'data' not in data or 'code' not in data:
        #     return jsonify({'res': False, 'msg': 'No data or code included'})

        work = Work(data=data['data'], code=data['code'], done=False)
        work.save()
        return jsonify({'res': True, 'msg': 'code uploaded'})


class KindleAPI(MethodView):

    def get(self):
        return jsonify({'res': True, 'Active': len(Kindle.objects())})

app.add_url_rule('/work/', view_func=WorkAPI.as_view('work'))
app.add_url_rule('/code/', view_func=CodeAPI.as_view('code'))
app.add_url_rule('/kindle/', view_func=KindleAPI.as_view('kindle'))
