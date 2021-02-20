from flask import request
from app.users.models import User, db
from app.utils.decorators import logging_decorator
from flask_jwt_extended import create_access_token, get_jwt_identity

@logging_decorator
def create_user():
    body = request.get_json()
    
    existing_user = User.query.filter_by(login=body["login"]).first()
    if existing_user is not None:
        return {"data": "User with login {} already exists".format(existing_user.login), "error": "error"}

    new_user = User(**body)
    new_user.generate_password()

    db.session.add(new_user)
    db.session.commit()

    return {"data": "User with login {} is created".format(str(new_user.login)), "error": "Ok"}

@logging_decorator
def login_user():
    body = request.get_json()
    existing_user = User.query.filter_by(login=body["login"]).first()
    if not existing_user:
        return {"data": 'User {} doesn\'t exist'.format(str(existing_user.login)), "error": "error"}
    elif existing_user.check_password(body["password"]):
        access_token = create_access_token(identity=existing_user.login)
        #login_user(user, remember=True)
        return {"access_token": access_token,"data": "{} is loggined".format(str(existing_user.login)), "error": "Ok"}
    else:
        return {"data": "Wrong credentials".format(str(user.login)), "error": "error"}

@logging_decorator
def logout_user():
    #logout_user()
    return {"data": "User is logout", "error": "Ok"}

@logging_decorator
def test_jwt():
    current_user = get_jwt_identity()
    return {"data": "HELLO {}".format(str(current_user)), "error": "OK"}
