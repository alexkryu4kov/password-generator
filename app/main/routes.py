from app.main import main_bp
from app.main.views import PasswordGeneratorView
from app.main.forms import GeneratePasswordForm

from flask import render_template
from flask_login import login_required


@main_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = GeneratePasswordForm()
    if form.validate_on_submit():
        password_generate_view = PasswordGeneratorView()
        return password_generate_view.dispatch_request()
    return render_template('index.html', form=form)


@main_bp.route('/password', methods=['GET', 'POST'])
@login_required
def generate_user_password():
    password_generate_view = PasswordGeneratorView()
    return password_generate_view.dispatch_request()

