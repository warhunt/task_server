from flask import Blueprint, request

import app.tasks.funcs as funcs

module = Blueprint('task', __name__, url_prefix ='/api/task')

@module.route('/', methods=['POST', 'GET'])
def create_get_all_task():
    if request.method == 'POST':
        return funcs.create_task()
    else:
        return funcs.get_all_task()

@module.route('/<int:task_id>', methods=['DELETE', 'PUT', 'GET'])
def delete_update_get_task(task_id):
    if request.method == 'DELETE':
        return funcs.delete_task(task_id)
    elif request.method == 'PUT':
        return funcs.update_task(task_id)
    else:
        return funcs.get_task(task_id)
