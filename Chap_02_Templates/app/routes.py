# app/routes.py

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Richard', 'name': 'Albert'}
    print(user['username'])

    posts = [
        {
            'author': 
            {
                'username': 'John',
                'name': 'Doe'
            },
            'body': 'Today is a beautiful day'
        }, 
        {
            'author': {
                'username': 'Susan',
                'name': 'Vega'
            },
            'body': 'Because the sun shine !'
        }
    ]
    
    title = 'Home Page'
    return render_template('index.html', title=title, user=user, posts=posts)


