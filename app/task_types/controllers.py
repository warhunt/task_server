from flask import Blueprint, request

import app.task_types.funcs as funcs

module = Blueprint('taskType', __name__, url_prefix ='/api/taskType')

@module.route("/", methods=['POST', 'GET'])
def create_get_all_taskType():
    if request.method == 'POST':
        return funcs.create_task_type()
    else:
        return funcs.get_all_task_type()

@module.route('/<int:task_type_id>', methods=['DELETE', 'PUT', 'GET'])
def delete_update_get_taskType(task_type_id):
    if request.method == 'DELETE':
        return funcs.delete_task_type(task_type_id)
    elif request.method == 'PUT':
        return funcs.update_task_type(task_type_id)
    else:
        return funcs.get_task_type(task_type_id)

