from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://andy:1@192.168.56.101:3306/employees'
db = SQLAlchemy(app)

from task import models, api