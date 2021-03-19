import os

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app
from app.database import db



app = create_app()
application = app.app
application.config.from_object(os.getenv('APP_SETTINGS'))

manager = Manager(application)
migrate = Migrate(application, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
    #app.run()
