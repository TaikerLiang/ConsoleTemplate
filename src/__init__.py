from config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://eb42d3a8cb5c4ccbad508ab218f695ea@sentry.io/1464180",
    integrations=[FlaskIntegration()]
)

app = Flask(__name__)

app = Flask(__name__)
app.config.from_object(config['development'])
db = SQLAlchemy(app)

from src import base
from src import user
