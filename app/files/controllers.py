from flask import Blueprint, request

import app.files.funcs as funcs

module = Blueprint('files', __name__, url_prefix ='/api/file')

@module.route('/', methods=['POST', 'GET'])
def create_get_all_file():
    if request.method == 'POST':
        return funcs.create_file()

@module.route('/<int:file_id>', methods=['DELETE', 'GET'])
def delete_update_get_file(file_id):
    if request.method == 'DELETE':
        return funcs.delete_file(file_id)
    if request.method == 'GET':
        return funcs.get_file(file_id)
