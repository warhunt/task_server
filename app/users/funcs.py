from flask import request
from flask_jwt_extended import create_access_token, get_jwt_identity

from app.users.models import User, db
from app.utils.decorators import logging_decorator
from app.utils.help_func import create_respons

@logging_decorator
def create_user():
    body = request.get_json()
    
    existing_user = User.query.filter_by(login=body["login"]).first()
    if existing_user is not None:
        return create_respons(error=1, message="User already exists")

    new_user = User(**body)
    new_user.generate_password()

    db.session.add(new_user)
    db.session.commit()

    return create_respons(message="User is created")

@logging_decorator
def get_all_users():
    all_users = User.query.all()

    if len(all_users) == 0:
        return create_respons(error=1, message="User table is empty")
    else:
        return create_respons(data=all_users)

@logging_decorator
def delete_user(id):
    existing_user = User.query.get_or_404(id)
   
    db.session.delete(existing_user)
    db.session.commit()

    return create_respons(message="User is deleted")

@logging_decorator
def update_user(id):
    body = request.get_json()

    existing_user = User.query.get_or_404(id)

    if User.query.filter_by(id=existing_user.id).update({**body}):
        if 'password' in body.keys():
            existing_user.generate_password()
        db.session.commit()
    else:
        return create_respons(error=1, message="What went wrong when updating a user")
    
    return create_respons(message="User is updated")

@logging_decorator
def get_user(id):
    existing_user = User.query.get_or_404(id)
    return create_respons(data=existing_user)

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
