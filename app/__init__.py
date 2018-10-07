""" Main Application file """
# Installed dependencies
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

# local modules
from config import config

# global vars
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


# The creation of the application is delayed until runtime by being
# put in a factory function, create_app(arg). This allows specification
# of configurations before the app is created
def create_app(config_name):
    # Define the WSGI application object
    app = Flask(__name__)
    # get configurations from config.py file
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # associate the blueprint with our app
    from main import main as main_blueprint
    from auth import auth as auth_blueprint

    # register all blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    # Build the database:
    # This will create the database file using SQLAlchemy
    with app.app_context():
        db.create_all()

    return app
