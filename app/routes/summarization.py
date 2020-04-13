from flask import request
from flask_restful import Resource
import os

class Summarizer(Resource):
    def post(self):
        data = request.get_json()

        return {'error': False, 'results': data}
