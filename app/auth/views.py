from flask import flash, render_template, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash
from .forms import LoginForm, RegistrationForm
from . import auth
from app.models.models import User
from app import db

@auth.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    error = None
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not user.verify_password(form.password.data):
            error = 'Invalid credentials'
        else:
            login_user(user)
            flash('You have been logged in')
            return redirect(url_for('main.index'))
    return render_template('auth/login.html', form = form, error = error)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form)
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('auth/register.html', form=form)