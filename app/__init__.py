import os
import logging
from logging.config import dictConfig

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS

from app.database import db
from app.jwt import jwt
import app.users.controllers as users
import app.roles.controllers as roles
import app.task_types.controllers as task_types
import app.tasks.controllers as tasks
import app.solutions.controllers as solutions
import app.files.controllers as files

def create_app():

    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))

    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    dictConfig(app.config['LOGGING'])
    app.logger = logging.getLogger(app.config['LOGGER_NAME'])
    db.init_app(app)
    
    jwt.init_app(app)
    
    with app.app_context():
        db.create_all()
        

    if app.debug == True:
        try:
            toolbar = DebugToolbarExtension(app)
        except:
            pass
    
    
    app.register_blueprint(users.module)
    app.register_blueprint(roles.module)
    app.register_blueprint(task_types.module)
    app.register_blueprint(tasks.module)
    app.register_blueprint(solutions.module)
    app.register_blueprint(files.module)

    return app