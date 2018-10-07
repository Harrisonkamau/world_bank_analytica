# Installed modules
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# local modules
from app import db, login_manager

"""
 - User class inherits from UserMixin which implements the methods
   such as is_authenticated(), is_active(), is_anonymous() and get_id()
 - db.Model has methods such as query which is being to retrieve a user
"""

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))


    # This callback function is required by Flask-Login to load a user
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Raise an exception when there is an attempt to read the
    # password attribute
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    # Implementation of the password hashing function in a write only
    # property password
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


class Catalog(object):
    pass
