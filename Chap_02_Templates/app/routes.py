# app/routes.py

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Richalbert'}
    print(user['username'])
    
    title = None
    return render_template('index.html', title=title, user=user)
    # return render_template('index.html', title='Home', user=user)

