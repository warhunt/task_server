from dataclasses import dataclass

from app.database import db, BaseModel

@dataclass
class File(db.Model, BaseModel):
    id: int
    created_on: str
    updated_on: str
    from_user_id: int
    file_name: str

    file_name = db.Column(db.String(50), nullable=False, unique=True)
    from_user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)

    def __str__(self):
        return self.file_name