from dataclasses import dataclass

from app.database import db, BaseModel

@dataclass
class Task(BaseModel, db.Model):
    id: int
    created_on: str
    updated_on: str 
    task_type_id: int
    from_user_id: int
    input_data: 'typing.Any'

    task_type_id = db.Column(db.Integer, db.ForeignKey('task_type.id'),
        nullable=False)
    from_user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    input_data = db.Column(db.JSON, nullable=False)

    created_by = db.relationship('User', backref='task', lazy=True)
    solutions = db.relationship('Solution', backref='task', lazy=True)
    
    
    def __str__(self):
        return self.id