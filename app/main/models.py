from app.db import db


class PasswordStorage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    site = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
