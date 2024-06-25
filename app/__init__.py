# app/__init__.py : Flask application instance

# from <package> import <module> 

# import a partir du package flask la classe Flask du module Flask
from flask import Flask

# on cree l'instance de la classe Flask
app = Flask(__name__)

# import de
from app import routes