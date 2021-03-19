from flask import request, jsonify

from app.solutions.models import Solution, db
from app.utils.decorators import logging_decorator
from app.utils.help_func import create_respons

@logging_decorator
def create_solution():
    body = request.get_json()

    new_solution = Solution(**body)
    db.session.add(new_solution)
    db.session.commit()
    return create_respons(message="Solution is created")

@logging_decorator
def get_all_solution():
    all_solution = Solution.query.all()

    if len(all_solution) == 0:
        return create_respons(error=1, message="Solution table is empty")
    else:
        return create_respons(data=all_solution)

@logging_decorator    
def delete_solution(solution_id):
    existing_solution = Solution.query.get_or_404(solution_id)
   
    db.session.delete(existing_solution)
    db.session.commit()
    return create_respons(message="Solution is deleted")

@logging_decorator
def update_solution(solution_id):
    body = request.get_json()

    existing_solution = Solution.query.get_or_404(solution_id)

    if Solution.query.filter_by(id=existing_solution.id).update({**body}):
        db.session.commit()
    else:
        return create_respons(error=1, message="What went wrong when updating a role")

    return create_respons(message="Role is updated")

@logging_decorator
def get_solution(solution_id):
    existing_solution = Solution.query.get_or_404(solution_id)
    return create_respons(data=existing_solution)