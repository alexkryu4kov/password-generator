from flask import Blueprint, render_template
from app.main.routes import PasswordGeneratorView


main_bp = Blueprint('main', __name__, template_folder='templates')


@main_bp.route('/')
def index():
    return render_template('index.html')
