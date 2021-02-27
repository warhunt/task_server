from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity

from app.tasks.models import Task, db
from app.utils.decorators import logging_decorator
from app.utils.help_func import create_respons

@logging_decorator
def create_task():
    body = request.get_json()
    
    new_task = Task(**body)
    db.session.add(new_task)
    db.session.commit()

    return create_respons(message="Task is created")

@logging_decorator
def get_all_task():
    all_task = Task.query.all()

    if len(all_task) == 0:
        return create_respons(error=1, message="Task table is empty")
    else:
        return create_respons(data=all_task)

@logging_decorator    
def delete_task(id):
    existing_task = Task.query.get_or_404(id)
   
    db.session.delete(existing_task)
    db.session.commit()

    return create_respons(message="Task is deleted")

@logging_decorator
def update_task(id):
    body = request.get_json()

    existing_task = Task.query.get_or_404(id)

    if Task.query.filter_by(id=existing_task.id).update({**body}):
        db.session.commit()
    else:
        return create_respons(error=1, message="What went wrong when updating a task")
    
    return create_respons(message="Task is updated")

@logging_decorator
def get_task(id):
    existing_task = Task.query.get_or_404(id)
    return create_respons(data=existing_task)