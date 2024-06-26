# app/routes.py

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Richalbert'}
    print(user['username'])
    return render_template('index.html', title='Home', user=user)
