from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__)
#app = application
application.config.from_object('config')
db = SQLAlchemy(application)

from app import views, models, foo