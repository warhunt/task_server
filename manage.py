import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app.database import db

app = create_app()
app.config.from_object(os.getenv('APP_SETTINGS'))

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    try:
        app.logger.info("FGSH_server started")
        manager.run()
    except Exception as ex:
            #.logger.warning(ex)
            print(ex)
    finally:
        app.logger.info("FGSH_server stoped")