import json
import pytest
import base64
import unittest
from src import app, db
from src.models import users
from pprint import pprint

def get_header(u):
    email_pw = "%s:%s" % (u.email, u.api_token)
    auth_pass = base64.b64encode(email_pw.encode('ascii'))
    headers = { 'Authorization' : 'Basic %s' %  auth_pass.decode("ascii")}

    return headers


def test_login(app_client, user):
    user = db.session.merge(user)
    data = {
        'email': 'paul@email.com',
        'password': 'paul@password',
        'login_token': ''
    }

    response = app_client.post('/login', data=data)
    #print(json.loads(response.get_data(as_text=True)))
    res = json.loads(response.get_data(as_text=True))
    assert res['err'] == 0


def test_dashboard(app_client, user):

    user = db.session.merge(user)
    response = app_client.get('/dashboard', headers=get_header(user))
    #print(response.get_data(as_text=True))
    res = json.loads(response.get_data(as_text=True))
    assert res['err'] == 0


