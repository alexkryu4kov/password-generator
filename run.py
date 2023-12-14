from app import create_app
from app.db import db
from app.login import login_bp
from app.login.models import User
from app.main import main_bp

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='testuser').first():
            user = User(username='testuser', password='your_password')
            db.session.add(user)
            db.session.commit()
    app.register_blueprint(main_bp)
    app.register_blueprint(login_bp)
    app.run(debug=True)
