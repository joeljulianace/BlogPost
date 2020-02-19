from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'f5707cb7053ec45aeaff95d7c6f8999f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:admin@localhost:5432/flaskblog'
db = SQLAlchemy(app)

from flaskblog import routes