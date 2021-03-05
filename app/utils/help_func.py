import os

from flask import current_app
from werkzeug.utils import secure_filename

def create_respons(message="", data=None, error=0):
    return {'data': data, 'error': error, 'message': message}

def __allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def save_file_to_dir(file):
    if file and __allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            return None

        file.save(file_path)
        return filename