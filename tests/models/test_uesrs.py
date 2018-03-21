import pytest
import time
from src import app, db
from src.models import users


@pytest.fixture(scope='module')
def user():
    user = users.User('taiker', 'taiker@email.com', 'taiker@password')
    db.session.add(user)
    db.session.commit()
    return user

def test_verify_password(user):
    assert user.verify_password('taiker@password') == True 


def test_login_auth_token(user):
    login_token = user.encode_login_auth_token()
    res = users.User.decode_login_auth_token(login_token.decode("utf-8"))
    assert res.email == user.email 


def test_api_auth_token(user):
    api_token = user.encode_api_auth_token()
    res = users.User.decode_api_auth_token(api_token.decode("utf-8"))
    assert res.email == user.email
    

def test_renew_last_login_date(user):
    time.sleep(2)
    user.renew_last_login_date()
