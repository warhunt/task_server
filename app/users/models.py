from dataclasses import dataclass

from werkzeug.security import generate_password_hash, check_password_hash

from app.database import db, BaseModel

@dataclass
class User(BaseModel, db.Model):
    id: int
    created_on: str
    updated_on: str 
    login: str
    _password: str
    role_id: int

    login = db.Column(db.String(25), nullable=False, unique=True)
    _password = db.Column(db.String(94))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),
        nullable=False)

    tasks = db.relationship('Task', backref='user', lazy=True)
    solutions = db.relationship('Solution', backref='user', lazy=True)
    files = db.relationship('File', backref='user', lazy=True)

    def check_password(self,  password):
        return check_password_hash(self._password, password)

    def generate_password(self):
        self.password = generate_password_hash(self.password)

    def __str__(self):
        return self.login
