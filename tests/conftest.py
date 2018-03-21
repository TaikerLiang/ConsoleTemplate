import pytest
from src import app, db
from src.models import users

@pytest.fixture(scope='session')
def user():
    print("user")
    user = users.User('paul', 'paul@email.com', 'paul@password')
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture(scope='session')
def app_client():
    print("app_client")
    return app.test_client()
