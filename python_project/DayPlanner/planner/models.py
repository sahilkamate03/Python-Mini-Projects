from email.policy import default
from enum import unique
from flask_login import UserMixin
from datetime import datetime
from planner import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    unique_id= db.Column(db.Text, nullable=False )
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    todos = db.relationship('Todo', backref='author',lazy = True)

    def __repr__(self) -> str:
        return f'User ({self.username}, {self.email})'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    date_posted = db.Column(db.String(10))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow())
    type = db.Column(db.String(1), default='R')
    user_id = db.Column(db.Text, db.ForeignKey(
        'user.id'))

    def __repr__(self) -> str:
        return f'Todo ({self.title}, {self.date_posted}, {self.time_posted})'
