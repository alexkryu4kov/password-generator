import os


class Config:
    SQLALCHEMY_DATABASE_URI = f"mysql://{os.environ['MYSQL_USER']}:{os.environ['MYSQL_PASSWORD']}@localhost:3306/{os.environ['MYSQL_DATABASE']}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'