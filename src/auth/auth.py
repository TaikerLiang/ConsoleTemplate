from functools import wraps
from flask import request, jsonify, abort, redirect, url_for
from src.models import users
from src import app


def check_auth(email, api_token):
    """
    Decodes the auth token for api request
    :param email:
    :param api_token:
    :return: integer
    """
    res = users.User.decode_api_auth_token(api_token)
    if isinstance(res, str):
        return 0
    else:
        return res.email == email


def requires_auth(f):
    """
    auth for api request 
    :return: function object
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            abort(401)
        return f(*args, **kwargs)
    return decorated
