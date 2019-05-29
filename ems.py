from app import app, db
from app.models import Employee, Project

@app.shell_context_processor
def make_shell_context():
    return {'db' : db, 'Employee' : Employee, 'Project' : Project}