import os
from flask import Flask
from app.database import db
import logging
from logging.config import dictConfig
from app.jwt import jwt

def create_app():

    app = Flask(__name__)
    app.config.from_object(os.getenv('APP_SETTINGS'))
    dictConfig(app.config['LOGGING'])
    app.logger = logging.getLogger(app.config['LOGGER_NAME'])
    db.init_app(app)
    jwt.init_app(app)
    
    with app.test_request_context():
        db.create_all()

    if app.debug == True:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass

    

    import app.users.controllers as users
    app.register_blueprint(users.module)
    
    return app