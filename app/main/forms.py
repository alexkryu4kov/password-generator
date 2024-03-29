from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, SubmitField, TextAreaField, StringField


class GeneratePasswordForm(FlaskForm):
    site = TextAreaField('Site', default='default')
    length = IntegerField('Password Length', default=15)
    uppercase = BooleanField('Uppercase', default=False)
    digits = BooleanField('Digits', default=False)
    symbols = BooleanField('Symbols', default=False)
    encrypted_password = StringField('Encrypted Password', default='')
    generate_password = SubmitField("Generate Password")
