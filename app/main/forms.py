from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SubmitField


class GeneratePasswordForm(FlaskForm):
    length = IntegerField('Password Length', default=15)
    uppercase = BooleanField('Uppercase', default=False)
    digits = BooleanField('Digits', default=False)
    symbols = BooleanField('Symbols', default=False)
    generate_password = SubmitField("Generate Password")
