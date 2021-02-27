from dataclasses import dataclass

from app.database import db, BaseModel

@dataclass
class Solution(BaseModel, db.Model):
    id: int
    created_on: str
    updated_on: str 
    task_id: int
    done_user_id: int
    output_data: 'typing.Any'

    task_id = db.Column(db.Integer, db.ForeignKey('task.id'),
        nullable=False)
    done_user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    output_data = db.Column(db.JSON, nullable=False)
    
    def __str__(self):
        return self.id