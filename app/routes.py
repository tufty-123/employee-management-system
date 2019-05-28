from app import app
from flask import render_template
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Sandesh'}
    users = ['Daksh', 'Sandesh', 'Prateek', 'Nishant', 'Tanmay', 'Jai', 'Shardul']
    return render_template('index.html', user=user, users=users)


@app.route('/profile')
def profile():
    return render_template('profile.html', title='Profile')


@app.route('/project')
def project():
    return render_template('project.html', title='Project')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='ContactUs')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)