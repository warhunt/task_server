import os
import logging
from logging.config import dictConfig

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_cors import CORS
import connexion

from app.database import db
from app.jwt import jwt
import app.users.controllers as users
import app.roles.controllers as roles
import app.task_types.controllers as task_types
import app.tasks.controllers as tasks
import app.solutions.controllers as solutions
import app.files.controllers as files

def create_app():

    #app = Flask(__name__)
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('openapi.yaml')
    application = app.app

    application.config.from_object(os.getenv('APP_SETTINGS'))

    cors = CORS(application, resources={r"/api/*": {"origins": "*"}})

    dictConfig(application.config['LOGGING'])
    application.logger = logging.getLogger(application.config['LOGGER_NAME'])
    db.init_app(application)
    
    jwt.init_app(application)
    
    with application.app_context():
        db.create_all()
        

    if application.debug == True:
        try:
            toolbar = DebugToolbarExtension(application)
        except:
            pass
    
    
    application.register_blueprint(users.module)
    application.register_blueprint(roles.module)
    application.register_blueprint(task_types.module)
    application.register_blueprint(tasks.module)
    application.register_blueprint(solutions.module)
    application.register_blueprint(files.module)

    return app