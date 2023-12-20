from flask import flash, render_template, request
from flask_login import current_user, login_required

from app.db import db
from app.main import main_bp
from app.main.forms import GeneratePasswordForm
from app.main.password_generator import PasswordGenerator
from app.main.models import PasswordStorage


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return render_template('index.html', username=current_user.username)
    return render_template('index.html')


@main_bp.route('/password_generation', methods=['GET', 'POST'])
@login_required
def password_generation():
    return render_template('password_generation.html')


@main_bp.route('/password', methods=['GET', 'POST'])
@login_required
def generate_user_password():
    form = GeneratePasswordForm(request.form)
    if form.validate_on_submit():
        length = form.length.data
        site = form.site.data
        uppercase = form.uppercase.data
        digits = form.digits.data
        symbols = form.symbols.data
        password = PasswordGenerator.generate_password(length, uppercase, digits, symbols)

        password_storage = PasswordStorage(user_id=current_user.id, site=site, password=password)
        db.session.add(password_storage)
        db.session.commit()
        flash(f"Generated Password: {password}", 'success')

    return render_template('password_generation.html', form=form)


@main_bp.route('/passwords', methods=['GET'])
@login_required
def user_passwords():
    passwords = PasswordStorage.query.filter_by(user_id=current_user.id).all()
    return render_template('user_passwords.html', passwords=passwords)
