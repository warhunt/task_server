from flask import request, jsonify
from app.roles.models import Role, db
from app.utils.decorators import logging_decorator
from flask_jwt_extended import create_access_token, get_jwt_identity
import datetime

@logging_decorator
def create_role():
    body = request.get_json()
    
    existing_role = Role.query.filter_by(role=body["role"]).first()
    if existing_role is not None:
        return {"data": "Role {} already exists".format(existing_role.role), "error": "error"}

    new_role = Role(**body)
    new_role.to_lower()
    db.session.add(new_role)
    db.session.commit()

    return {"data": "Role {} is created".format(str(new_role.role)), "error": "Ok"}

@logging_decorator
def get_all_roles():
    all_role = Role.query.all()

    if len(all_role) == 0:
        return {"data": "Role table is empty", "error": "error"}
    else:
        return {"data": all_role, "error": "Ok"}

@logging_decorator    
def delete_role(id):
    existing_role = Role.query.get_or_404(id)
   
    db.session.delete(existing_role)
    db.session.commit()

    return {"data": "Role {} is deleted".format(str(existing_role.role)), "error": "Ok"}

@logging_decorator
def update_role(id):
    body = request.get_json()

    existing_role = Role.query.get_or_404(id)

    existing_role.role = body['role']
    existing_role.created = datetime.datetime.now()
    db.session.commit()

    return {"data": "Role {} is updated".format(str(existing_role.role)), "error": "Ok"}

@logging_decorator
def get_role(id):
    existing_role = Role.query.get_or_404(id)
    print(existing_role.users)
    return {"data": existing_role, "error": "Ok"}