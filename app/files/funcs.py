import os 

from flask import request, jsonify, current_app, send_from_directory

from app.files.models import File, db
from app.utils.decorators import logging_decorator
from app.utils.help_func import create_respons, save_file_to_dir

@logging_decorator
def create_file():
    body = request.form.to_dict()
    if 'file' not in request.files:
        return create_respons(error=1, message='No file part')

    input_file = request.files['file']

    new_file_name = save_file_to_dir(input_file)

    if new_file_name is None:
        return create_respons(error=1, message='File with this name exist or format of file is not valid')

    body['file_name'] = new_file_name

    new_file = File(**body)

    db.session.add(new_file)
    db.session.commit()

    return create_respons(message="File is created")

@logging_decorator
def get_file(id):
    existing_file = File.query.get_or_404(id)

    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], existing_file.file_name)

    if not os.path.exists(file_path):
        db.session.delete(existing_file)
        db.session.commit()
        return create_respons(error=1, message="File is not exist")
        
    return send_from_directory("static/upload", existing_file.file_name)

@logging_decorator
def delete_file(id):
    existing_file = File.query.get_or_404(id)

    file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], existing_file.file_name)

    if not os.path.exists(file_path):
        return create_respons(error=1, message="File is not exist")
    
    os.remove(os.path.join(current_app.config['UPLOAD_FOLDER'], existing_file.file_name))

    db.session.delete(existing_file)
    db.session.commit()

    return create_respons(message="File is deleted")
