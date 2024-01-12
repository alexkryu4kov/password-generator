from flask import current_app, flash, render_template, request, jsonify
from flask_login import current_user, login_required

from app.db import db
from app.main import main_bp
from app.main.forms import GeneratePasswordForm
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
def generate_user_password():
    form = GeneratePasswordForm(request.form)
    if form.validate_on_submit():
        site = form.site.data
        encrypted_password = form.encrypted_password.data
        password_storage = PasswordStorage(user_id=current_user.id, site=site, password=encrypted_password)
        db.session.add(password_storage)
        db.session.commit()
        flash(f"Generated Password: {encrypted_password}", 'success')

    return render_template('password_generation.html', form=form)


@main_bp.route('/passwords', methods=['GET'])
@login_required
def user_passwords():
    passwords = PasswordStorage.query.filter_by(user_id=current_user.id).all()
    return render_template('user_passwords.html', passwords=passwords)


@main_bp.route('/test_db_connection', methods=['GET'])
def test_db_connection():
    try:
        db.session.execute('SELECT 1')
        return jsonify({'message': 'Database connection successful'})
    except Exception as e:
        return jsonify({'message': f'Database connection error: {str(e)}'}), 500
