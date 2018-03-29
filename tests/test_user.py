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

def test_get(app_client, user):
    user = db.session.merge(user)
    data = {
        'email': 'paul@email.com',
    }
    
    response = app_client.get('/user', query_string=data, headers=get_header(user))
    #print(json.loads(response.get_data(as_text=True)))
    res = json.loads(response.get_data(as_text=True))
    assert res['err'] == 0

def test_post(app_client, user):

    data = {
        'name': 'paul2',
        'email': 'paul2@email.com',
        'password': 'paul2@password',
    }

    response = app_client.post('/user', data=data)
    #print(json.loads(response.get_data(as_text=True)))
    res = json.loads(response.get_data(as_text=True))
    assert res['err'] == 0

def test_put(app_client, user):
    user = db.session.merge(user)
    data = {
        'email': 'paul@email.com',
        'name': 'paul2'
    }

    response = app_client.put('/user', data=data, headers=get_header(user))
    #print(json.loads(response.get_data(as_text=True)))
    res = json.loads(response.get_data(as_text=True))
    assert res['err'] == 0

def test_delete(app_client, user):
    user = db.session.merge(user)
    data = {
        'email': 'paul@email.com',
    }

    response = app_client.delete('/user', data=data, headers=get_header(user))
    #print(json.loads(response.get_data(as_text=True)))
    res = json.loads(response.get_data(as_text=True))
    assert res['err'] == 0
