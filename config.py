import os
from logging import DEBUG as log_debug

class Config:
    DEBUG = False

    # Случайный ключ, которые будет исползоваться для подписи
    # данных, например cookies.
    SECRET_KEY = os.getenv('SECRET_KEY')

    # URI используемая для подклюечния к базе данных
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #под для генерации JWT
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

    #переменные для логирования приложения
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