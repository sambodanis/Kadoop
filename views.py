from flask import Blueprint, request, redirect, render_template, url_for, jsonify
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form

from Kadoop.models import Kindle, Work, Code
from Kadoop import app

import json
import datetime


class WorkAPI(MethodView):

    def get(self):
        work_piece = Work.objects(taken=False).first()
        if work_piece:
            data = work_piece.data
            code = work_piece.code.code
            if 'id' in request.values:
                kindle = Kindle.objects(uuid=request.values['id'])
            else:
                return jsonify({
                               'res': False
                               })
            work_piece.kindle = kindle[0]

            work_id = str(work_piece.kindle.id)

            response_object = {
                'res': True, 'data': data, 'code': code, 'work_id': work_id}
            work_piece.taken = True
            work_piece.save()
        else:
            response_object = {
                'res': False
            }

        return jsonify(response_object)

    def post(self):
        data = request.values
        if 'id' in data and 'active' in data:
            uuid = data['id']
            active = data['active']
            kindle = Kindle.objects.get_or_create(
                uuid=uuid, active=active)[0]
            kindle.active = True
            print 'Kindle with id %s added' % kindle.uuid
            kindle.save()
            return jsonify({'res': True, 'msg': 'Kindle Activated'})
        return jsonify({'res': False, 'msg': 'No id included'})


class CodeAPI(MethodView):

    def chunks(self, l, n):
        if n < 1:
            n = 1
        return [l[i:i + n] for i in range(0, len(l), n)]

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
        if 'data' not in data or 'code' not in data:
            return jsonify({'res': False, 'msg': 'No data or code included'})

        code = Code(data['code'])
        code.save()
        num_devices = len(Kindle.objects())
        split_data = self.chunks(data['data'], len(data['data']) / num_devices)
        for sub_data in split_data:
            work = Work(data=sub_data, code=code, taken=False, done=False)
            work.save()
        return jsonify({'res': True, 'msg': 'code uploaded'})


class KindleAPI(MethodView):

    def get(self):
        return jsonify({'res': True, 'active': len(Kindle.objects())})

    def post(self):
        data = request.get_json(force=True)
        if 'result' not in data or 'work_id' not in data:
            return jsonify({'res': False, 'msg': 'No work or work_id included'})

        work_id = data['work_id']
        data = data['result']
        work = Work.objects(id=work_id)
        work.data = work
        work.taken = True
        work.done = True
        work.save()

        return jsonify({'res': True, 'msg': 'work recieved'})

app.add_url_rule('/work/', view_func=WorkAPI.as_view('work'))
app.add_url_rule('/code/', view_func=CodeAPI.as_view('code'))
app.add_url_rule('/kindle/', view_func=KindleAPI.as_view('kindle'))
