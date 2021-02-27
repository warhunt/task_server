from flask import Blueprint, request
from flask_jwt_extended import jwt_required

import app.users.funcs as funcs

module = Blueprint('users', __name__, url_prefix ='/api/user')

@module.route("/", methods=['POST', 'GET'])
def create_get_all_user():
    if request.method == 'POST':
        return funcs.create_user()
    else:
        return funcs.get_all_users()

@module.route('/<int:user_id>', methods=['DELETE', 'PUT', 'GET'])
def delete_update_get_user(user_id):
    if request.method == 'DELETE':
        return funcs.delete_user(user_id)
    elif request.method == 'PUT':
        return funcs.update_user(user_id)
    else:
        return funcs.get_user(user_id)

@module.route("/login", methods=["POST"])
def login_user():
    return funcs.login_user()

@module.route("/logout")
def logout_user():
    return funcs.logout_user()

@module.route("/protect")
@jwt_required()
def test_jwt():
    return funcs.test_jwt()