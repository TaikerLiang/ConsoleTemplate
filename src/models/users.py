"""
.. module:: user
   :platform: Ubuntu 16.04, linux & Mac OS
   :synopsis: mapping to user table in database

.. moduleauthor:: Paul Liang <liang0816tw@gmail.com>
.. date:: 2018-03-16
"""

from src import app
from src import db
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import Column, Integer, String, DateTime
from pprint import pprint
import jwt
import datetime


class User(db.Model):

    __tablename__ = 'users'

    # table columns
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    api_token = Column(String)
    status = Column(Integer)
    create_time = Column(DateTime)
    last_login = Column(DateTime)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = self.hash_password(password)
        self.create_time = datetime.datetime.now()
        self.last_login = datetime.datetime.now()
        self.api_token = ''
        self.status = 0

    def hash_password(self, password):
        """
        hash user password
        :return: string
        """
        return pwd_context.encrypt(password + app.config['LOGIN_SECRET_KEY'])

    def verify_password(self, password):
        """
        get user password from db and hash it then ruturn.
        :return: string
        """
        return pwd_context.verify(
            password + app.config['LOGIN_SECRET_KEY'], self.password)

    def encode_login_auth_token(self):
        """
        Generates the auth token for login
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.now() +
                datetime.timedelta(hours=6, seconds=0),
                'iat': datetime.datetime.now(),
                'sub': self.email
            }

            return jwt.encode(
                payload,
                app.config['LOGIN_SECRET_KEY'],
                algorithm='HS256'
            )

        except Exception as e:
            return e

    @staticmethod
    def decode_login_auth_token(auth_token):
        """
        Decodes the auth token for login
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config['LOGIN_SECRET_KEY'])
            user = User.query.filter_by(email=payload['sub']).first()
            return user
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def encode_api_auth_token(self):
        """
        Generates the auth token for api
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.now() +
                datetime.timedelta(hours=6, seconds=0),
                'iat': datetime.datetime.now(),
                'sub': self.email
            }

            return jwt.encode(
                payload,
                app.config['API_SECRET_KEY'],
                algorithm='HS256'
            )

        except Exception as e:
            return e

    @staticmethod
    def decode_api_auth_token(auth_token):
        """
        Decodes the auth token for api
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config['API_SECRET_KEY'])
            user = User.query.filter_by(email=payload['sub']).first()
            return user
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    def renew_last_login_date(self):
        """
        record user last login time
        :return: None
        """
        self.last_login = datetime.datetime.now()
        db.session.commit()

    def renew_api_token(self, api_token):
        """
        record user new api token
        :return: None
        """
        self.api_token = api_token
        db.session.commit()
