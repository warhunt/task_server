import app.users.funcs as funcs
from flask import Blueprint
from flask_jwt_extended import jwt_required

module = Blueprint('users', __name__, url_prefix ='/api/user')

@module.route("/create", methods=["POST"])
def create_user():
    return funcs.create_user()

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