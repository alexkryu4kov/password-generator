from app.main.password_generator import PasswordGenerator
from flask.views import View
from flask import render_template

from app.main.forms import GeneratePasswordForm


class PasswordGeneratorView(View):

    def dispatch_request(self):

        form = GeneratePasswordForm()
        if form.validate_on_submit():
            password = PasswordGenerator.generate_password()
            return render_template('generate_password.html', password=next(password), form=form)
        return render_template('generate_password.html', form=form)
