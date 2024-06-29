# app/__init__.py 

from flask import Flask
app = Flask(__name__)


# app.config['SECRET_KEY'] = 'mon_jeton_CSRF'   # jeton CSRF
from config import Config
app.config.from_object(Config)


from app import routes

