""" Server file """

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server

from app import create_app, db

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

# fire up server
if __name__ == '__main__':
    manager.run()
