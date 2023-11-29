import string
import random


class PasswordGenerator:

    @classmethod
    def generate_password(cls):
        all_symbols = string.ascii_letters
        while True:
            password = ''.join(random.choice(all_symbols) for _ in range(15))
            yield password
