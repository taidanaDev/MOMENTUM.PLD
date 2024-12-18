from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Classified Database Model for the User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # Primary Key for the user
    email = db.Column(db.String(150), unique=True, nullable=False)  # Ensure email is not nullable
    username = db.Column(db.String(150), unique=True, nullable=False)  # Username must be unique and not nullable
    password = db.Column(db.String(150), nullable=False)  # Password should be required
    name = db.Column(db.String(150), nullable=True)  # Name can be optional
    tasks = db.relationship('Task', backref='user', lazy=True)  

# Classified Database Model for the Task
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)    # Primary Key for the task
    title = db.Column(db.String(100), nullable=False)  # Task title is required
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.Date, nullable=False, default=func.now())  # Default to current date
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_done = db.Column(db.Boolean, default=False)  # Defaults to not done
