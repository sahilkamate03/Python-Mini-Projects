from todo import db
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    todos = db.relationship('Todo', backref='author')

    def __repr__(self) -> str:
        return f'User ({self.username}, {self.email})'


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    date_posted = db.Column(db.String(10))
    time_posted = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.String(100), db.ForeignKey(
        'user.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Todo ({self.title}, {self.date_posted}, {self.time_posted})'
