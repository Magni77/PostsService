import jwt
from bottle import route, request, abort

from api.settings import SECRET


def decode_jwt(token):
    token = token.split()[1]
    return jwt.decode(token, SECRET, algorithm='HS256')


def login_required(func):
    def login_wrapper(*args, **kwargs):
        token = request.headers.get('authorization')
        if not token:
            abort(401, 'Access denied')
        user_data = decode_jwt(token)
        return func(user_data, *args, **kwargs)

    return login_wrapper
