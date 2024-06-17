# app/routes.py : Home page route

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Richalbert'}
    # page = render_template('index.html', title='Home Page', user=user, toto='toto')
    page = render_template('index.html', user=user, toto='toto')
    return page