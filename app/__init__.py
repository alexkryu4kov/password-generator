from flask import Flask
from flask_login import LoginManager

from app.db import db
from app.login import login_bp
from app.login.models import User
from app.main.routes import PasswordGeneratorView
from app.main import main_bp

from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.main.config.Config')

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)

    migrate = Migrate(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    return app
