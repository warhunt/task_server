from app.database import db
import datetime
from dataclasses import dataclass

@dataclass
class Role(db.Model):
    id: int
    role: str
    created: datetime.datetime

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(25), nullable=False, unique=True)
    created = db.Column(db.DateTime, default=datetime.datetime.now)

    users = db.relationship('User', backref='role', lazy='dynamic')

    def to_lower(self):
        self.role = self.role.lower()

    def __str__(self):
        return self.role