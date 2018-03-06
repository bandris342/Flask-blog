from flask import Flask
from app.models import db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
db.create_all(app=app)

from app import views