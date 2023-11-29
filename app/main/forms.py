from flask_wtf import FlaskForm
from wtforms import SubmitField


class GeneratePasswordForm(FlaskForm):
    generate_password = SubmitField("Generate Password")
