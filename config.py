import os
from logging import DEBUG as log_debug

class Config:
    DEBUG = False

    # A random key that will be used to sign data, such as cookies.
    SECRET_KEY = os.getenv('SECRET_KEY')

    # URI used to connect to the database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #secret code for JWT generation
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    #variables for logging the application
    LOGGER_NAME = 'FGSH_server'
    LOGGING = {
        'version': 1,
        'formatters': {
            'default': {
                'format': "[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s",
            },
        },

        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': 'app/FGSH_server_log.log',
            },
        },
        'loggers': {
            'FGSH_server': {
                'handlers': ['file', ],
                'level': log_debug
            },
        },
    }

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
