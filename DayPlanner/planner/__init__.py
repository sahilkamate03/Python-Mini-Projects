from authlib.integrations.flask_client import OAuth
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('TODO_FLASK_SECRET_KEY')
uri = os.getenv("DATABASE_URL")  
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri

db = SQLAlchemy(app)
SQLALCHEMY_TRACK_MODIFICATIONS = False
login_manager = LoginManager(app)
login_manager.login_view = 'login'
oauth = OAuth(app)

from planner import routes