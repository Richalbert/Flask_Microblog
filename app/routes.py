# app/routes.py : Home page route


from app import app


@app.route('/')
@app.route('/index')
def index():

    user = {'username': 'Richalbert'}
    page = '''
    <htm>
        <head>
            <title>Home Page - MicroBlog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''
    return page