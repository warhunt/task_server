from dataclasses import dataclass

from app.database import db, BaseModel

@dataclass
class Role(BaseModel, db.Model):
    id: int
    created_on: str
    updated_on: str 
    role: str

    role = db.Column(db.String(25), nullable=False, unique=True)

    users = db.relationship('User', backref='role', lazy=True)

    def to_lower(self):
        self.role = self.role.lower()

    def __str__(self):
        return self.role