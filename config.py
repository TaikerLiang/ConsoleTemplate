import logging

class Config(object):
    DEVELOPMENT = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # change API_SECRET_KEY for your own appliaction
    API_SECRET_KEY = '4p2itrn3k9axbz4ts8f92vlzw4m30949k9sg5cum'
    # change LOGIN_SECRET_KEY for your own appliaction
    LOGIN_SECRET_KEY = 'qjugiycmyfgqhqfvmnpw8qntlewxexp7xghiwvi7'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'YOURAPP.log'
    LOGGING_LEVEL = logging.DEBUG

class ProductionConfig(Config):
    DEBUG = False
    DOMAIN = 'http://127.0.0.1:5000'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    DOMAIN = 'http://127.0.0.1:5000'
    SQLALCHEMY_DATABASE_URI = 'postgresql://taiker:@localhost/basic'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    DOMAIN = 'http://127.0.0.1:5000'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../flask.db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
