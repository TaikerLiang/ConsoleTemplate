from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config['development'])
db = SQLAlchemy(app)

from src import base
