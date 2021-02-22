from app.database import db
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from dataclasses import dataclass

@dataclass
class User(db.Model):
    id: int
    login: str
    password: str
    created: datetime.datetime
    role_id: int

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(94))
    created = db.Column(db.DateTime, default=datetime.datetime.now)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),
        nullable=False)

    def check_password(self,  password):
        return check_password_hash(self.password, password)

    def generate_password(self):
        self.password = generate_password_hash(self.password)

    def __str__(self):
        return self.login
