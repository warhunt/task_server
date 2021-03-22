from dataclasses import dataclass

from app.database import db, BaseModel

@dataclass
class TaskType(BaseModel, db.Model):
    id: int
    created_on: str
    updated_on: str 
    name: str
    input_data_type: 'typing.Any'
    output_data_type: 'typing.Any'

    name = db.Column(db.String(150), nullable=False, unique=True)
    input_data_type = db.Column(db.JSON, nullable=False)
    output_data_type = db.Column(db.JSON, nullable=False) 

    tasks = db.relationship('Task', backref='task_type', lazy=True)

    def __str__(self):
        return self.name
