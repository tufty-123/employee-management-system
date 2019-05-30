"""
Database Models
This module contains different database class models defined in the project.
"""


from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login


class Project(db.Model):
    """
    Project class pertaining to Project Table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(256))
    status = db.Column(db.String(120))
    #Setting up one to many relationship between project and employee
    member = db.relationship('Employee', backref='project', lazy='dynamic')

    def __repr__(self):
        return 'Project {}'.format(self.name)


class Employee(UserMixin, db.Model):
    """
    Employee class pertaining to Employee Table
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    name = db.Column(db.String(120))
    contact = db.Column(db.Integer)
    address = db.Column(db.String(120))
    manager = db.Column(db.String(120))
    #project_id is foreign key to class Project
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User {}'.format(self.username)


@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))