from app import create_app
from app.db import db
from app.login import login_bp
from app.main import main_bp

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)
    app.run(debug=True)
