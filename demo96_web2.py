# encoding=UTF-8
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Rest1(Resource):
    def get(self):
        return {'course': 'bdpy', 'duration': 35, 'instructor': '何馬克'}


class Rest2(Resource):
    def get(self):
        return ['BDPY', 'BDR', 'AndBiz', 'AppSec', 'PYKT', 'RKT']


api.add_resource(Rest1, '/course')
api.add_resource(Rest2, '/mark')

app.run(port=5002, host='0.0.0.0', debug=True)