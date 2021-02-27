from flask import request

from app.task_types.models import TaskType, db
from app.utils.decorators import logging_decorator
from app.utils.help_func import create_respons

@logging_decorator
def create_task_type():
    body = request.get_json()
    
    existing_task_type = TaskType.query.filter_by(name=body["name"]).first()
    if existing_task_type is not None:
        return create_respons(error=1, message="Task type already exists")

    new_task_type = TaskType(**body)

    db.session.add(new_task_type)
    db.session.commit()

    return create_respons(message="Task type is created")

@logging_decorator
def get_all_task_type():
    all_task_types = TaskType.query.all()

    if len(all_task_types) == 0:
        return create_respons(error=1, message="TaskType table is empty")
    else:
        return create_respons(data=all_task_types)

@logging_decorator
def delete_task_type(id):
    existing_task_type = TaskType.query.get_or_404(id)
   
    db.session.delete(existing_task_type)
    db.session.commit()

    return create_respons(message="Task type is deleted")

@logging_decorator
def update_task_type(id):
    body = request.get_json()

    existing_task_type = TaskType.query.get_or_404(id)

    if TaskType.query.filter_by(id=existing_task_type.id).update({**body}):
        db.session.commit()
    else:
        return create_respons(error=1, message="What went wrong when updating a task_type")
    
    return create_respons(message="Task type is updated")

@logging_decorator
def get_task_type(id):
    existing_task_type = TaskType.query.get_or_404(id)
    return create_respons(data=existing_task_type)

