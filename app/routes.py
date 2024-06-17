# app/routes.py : Home page route

from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Richalbert'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': "Today it's a beautiful day"
        },
        {
            'author': {'username': 'Susan'},
            'body': "Because the sun shine"
        }
    ]
    # page = render_template('index.html', title='Home Page', user=user, toto='toto')
    # page = render_template('index.html', user=user, toto='toto')
    page = render_template('index.html', user=user, posts=posts)
    return page