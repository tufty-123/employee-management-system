"""
Forms Module containing class models for different Forms used in the project.
"""


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import Employee


class LoginForm(FlaskForm):
    """
    This class represents the Login form present in login.html
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    """
    This class represents the registration form present in register.html
    """
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    contact = IntegerField('Contact', validators=[DataRequired()])
    address = StringField('Address')
    manager = StringField('Manager')
    submit = SubmitField('Register')

    def validate_username(self, username):
        employee = Employee.query.filter_by(username=username.data).first()
        if employee is not None:
            raise ValidationError('Please select a different username.')

    def validate_email(self, email):
        employee = Employee.query.filter_by(email=email.data).first()
        if employee is not None:
            raise ValidationError('Please select a different email address.')


class ProjectForm(FlaskForm):
    """
    This class represents the project form present in project.html
    """
    choice = SelectField('Select Project', validators=[DataRequired()])
    submit = SubmitField('Add Project')
