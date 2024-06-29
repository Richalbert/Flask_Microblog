# app/routes.py

from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Richard', 'name': 'Albert'}
    # print(user['username'])

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


# Login view funtion
from app.forms import LoginForm
from flask import flash, redirect, url_for

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        #flash('Login requested for user {}, remember_={}'.format(form.username.data, form.remember_me.data))
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))

    return render_template('login.html', title='Sign In', form=form)
