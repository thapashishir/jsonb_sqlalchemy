from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db_url='postgresql+psycopg2://postgres:passwd@localhost:5432/test_db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)

from jsonb_app.views import *
