from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm, ProjectForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Employee, Project
from werkzeug.urls import url_parse


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='HomePage')


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', title='Profile')


@app.route('/project', methods=['GET', 'POST'])
@login_required
def project():
    form = ProjectForm()
    projects = Project.query.all()
    form.choice.choices = [(p.name, p.name) for p in projects]
    employee = Employee.query.filter_by(id=current_user.id).first()

    if form.validate_on_submit():
        choice = form.choice.data
        print(choice)
        p = Project.query.filter_by(name=choice).first()
        if p is not None:
            employee = Employee.query.filter_by(id=current_user.id).first()
            employee.project = p
            db.session.add(employee)
            db.session.commit()
            flash('Project Added Successfully')
        return redirect(url_for('index'))
    return render_template('project.html', title='Project',
                           form=form, project=employee.project)


@app.route('/contact')
@login_required
def contact():
    return render_template('contact.html', title='ContactUs')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()

    if form.validate_on_submit():
        employee = Employee.query.filter_by(
            username=form.username.data).first()
        if employee is None or not employee.check_password(
            form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))
        login_user(employee, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(username=form.username.data,
                            email=form.email.data,
                            name=form.name.data,
                            contact=form.contact.data,
                            address=form.address.data,
                            manager=form.manager.data)
        employee.set_password(form.password.data)
        db.session.add(employee)
        db.session.commit()
        flash('Congratulations! You are now a registered user')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
