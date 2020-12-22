from flask import render_template

from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Jose Luis'}
    posts = [
        {
            'autor': {'username': 'Juan'},
            'body': 'Un día estupendo en Tomelloso!'
        },
        {
            'autor': {'username': 'Elena'},
            'body': 'Ayer vi una película fantastica'
        }

    ]
    return render_template('index.html', title='Home', user=user, posts=posts)