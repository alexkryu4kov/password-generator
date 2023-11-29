from app.main.password_generator import PasswordGenerator

from flask.views import View


class PasswordGeneratorView(View):

    def dispatch_request(self):
        password = PasswordGenerator.generate_password()
        return next(password)
