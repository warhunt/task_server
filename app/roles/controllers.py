from flask import Blueprint, request

import app.roles.funcs as funcs

module = Blueprint('roles', __name__, url_prefix ='/api/role')

@module.route('/', methods=['POST', 'GET'])
def create_get_all_role():
    if request.method == 'POST':
        return funcs.create_role()
    else:
        return funcs.get_all_roles()

@module.route('/<int:role_id>', methods=['DELETE', 'PUT', 'GET'])
def delete_update_get_role(role_id):
    if request.method == 'DELETE':
        return funcs.delete_role(role_id)
    elif request.method == 'PUT':
        return funcs.update_role(role_id)
    else:
        return funcs.get_role(role_id)
