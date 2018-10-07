from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, PasswordField
from wtforms.validators import Required, EqualTo, Length, Regexp, Email
from app.models.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    username = StringField('Username', validators=[Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                     'Usernames must have only letters,'
                                                                                     'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[Required(), EqualTo('password2', message="Passwords must match")])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use')

