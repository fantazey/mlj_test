from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from task.config import CONNECTION_STR

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONNECTION_STR
db = SQLAlchemy(app)

from task import models, api