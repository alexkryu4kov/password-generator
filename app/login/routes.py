from flask import current_app, flash, redirect, render_template, request, url_for, session
from flask_login import current_user, login_required, login_user, logout_user
from flask_wtf import csrf

from app.db import db
from app.login import login_bp
from app.login.forms import LoginForm, RegistrationForm
from app.login.models import User


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    # if not session.get('csrf_token'):
    #    csrf.generate_csrf()
    if form.validate_on_submit():
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Login failed', 'danger')
    return render_template('login/login.html', form=form)


@login_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'success')
    return redirect(url_for('main.index'))


@login_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    # csrf.generate_csrf()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)

        db.session.add(user)
        db.session.commit()

        flash('Your account has been created!', 'success')
        return redirect(url_for('login.login'))
    return render_template('login/register.html', title='Register', form=form)
