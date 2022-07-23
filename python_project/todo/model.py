from app import db
from datetime import datetime

class todo(db.Model):
    id = db.Column(db.Interger, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    time_posted = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self) -> str:
        return f'Todo ({self.title}, {self.time_posted})'