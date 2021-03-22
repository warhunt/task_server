from flask import request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity

from app.roles.models import Role, db
from app.utils.decorators import logging_decorator
from app.utils.help_func import create_respons

@logging_decorator
def create_role():
    body = request.get_json()
    
    existing_role = Role.query.filter_by(role=body["role"]).first()
    if existing_role is not None:
        return jsonify(create_respons(message="Role already exists", error=1)), 409

    new_role = Role(**body)
    new_role.to_lower()
    db.session.add(new_role)
    db.session.commit()

    return jsonify(create_respons(message="Role is created")), 201

@logging_decorator
def get_all_roles():
    all_role = Role.query.all()

    if len(all_role) == 0:
        return create_respons(message="Role table is empty", error=1)
    else:
        return create_respons(data=all_role)

@logging_decorator    
def delete_role(role_id):
    existing_role = Role.query.get_or_404(role_id)
   
    db.session.delete(existing_role)
    db.session.commit()

    return create_respons(message="Role is deleted")

@logging_decorator
def update_role(role_id):
    body = request.get_json()

    existing_role = Role.query.get_or_404(role_id)

    if Role.query.filter_by(id=existing_role.id).update({**body}):
        db.session.commit()
    else:
        return create_respons(error=1, message="What went wrong when updating a role")
    return create_respons(message="Role is updated")

@logging_decorator
def get_role(role_id):
    existing_role = Role.query.get_or_404(role_id)
    return create_respons(data=existing_role)