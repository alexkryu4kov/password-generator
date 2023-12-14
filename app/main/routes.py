from flask import flash, render_template, request
from flask_login import current_user, login_required

from app.main import main_bp
from app.main.forms import GeneratePasswordForm
from app.main.password_generator import PasswordGenerator


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
        uppercase = form.uppercase.data
        digits = form.digits.data
        symbols = form.symbols.data
        password = PasswordGenerator.generate_password(length, uppercase, digits, symbols)

        flash(f"Generated Password: {password}", 'success')

    return render_template('password_generation.html', form=form)
