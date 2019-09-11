from flask import request
from flask_restful import Resource
import requests

from controllers.jwt_validator import validate_jwt
from secrets_apis import YANDEX_TRANSLATE_API_KEY


class Translate(Resource):
    def post(self):
        data = request.get_json()
        is_valid = None
        try:
            is_valid = validate_jwt(request.headers['Authorization'])
        except:
            return {'error': True, 'errorMessage': 'Invalid access_token'}, 400

        if not is_valid:
            return {'error': True, 'errorMessage': 'Invalid access_token'}, 400

        lang = data['lang']
        text = data['text']

        r = requests.get(
            f'https://translate.yandex.net/api/v1.5/tr.json/translate?key={YANDEX_TRANSLATE_API_KEY}&text={text}&lang={lang}&options=1')

        r_data = r.json()
        del r_data['code']

        return {'error': False, 'results': r_data}
