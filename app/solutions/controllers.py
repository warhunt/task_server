from flask import Blueprint, request

import app.solutions.funcs as funcs

module = Blueprint('solutions', __name__, url_prefix ='/api/solution')

@module.route('/', methods=['POST', 'GET'])
def create_get_all_solution():
    if request.method == 'POST':
        return funcs.create_solution()
    else:
        return funcs.get_all_solution()

@module.route('/<int:solution_id>', methods=['DELETE', 'PUT', 'GET'])
def delete_update_get_solution(solution_id):
    if request.method == 'DELETE':
        return funcs.delete_solution(solution_id)
    elif request.method == 'PUT':
        return funcs.update_solution(solution_id)
    else:
        return funcs.get_solution(solution_id)
