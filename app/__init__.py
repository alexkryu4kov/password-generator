import logging
import sys

from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

from dotenv import load_dotenv

from app.db import db, migrate
from app.login import login_bp
from app.login.models import User
from app.main import main_bp


def get_console_logger_handler():

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    return console_handler


load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config.from_object('app.main.config.Config')

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    migrate.init_app(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)

    console_handler = get_console_logger_handler()
    app.logger.addHandler(console_handler)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
