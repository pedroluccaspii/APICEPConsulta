from flask import Flask
from flask_sqlalchemy import  SQLAlchemy
from flask_migrate import Migrate
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(base_dir, 'endereco.db')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{database_path}'
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)



