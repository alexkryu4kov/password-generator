import random
import string

from app.logger import get_logger

logger = get_logger()


class PasswordGenerator:

    @classmethod
    def generate_password(cls, length=15, uppercase=False, digits=False, symbols=False):
        # TODO: autofill parameters based on previous site usage
        password = ''.join(random.choice(string.ascii_letters).lower() for _ in range(length))
        logger.info(f'Original password: {password}')

        if uppercase:
            password = cls._insert_uppercase(password)

        if digits:
            password = cls._insert_number(password)

        if symbols:
            password = cls._insert_symbol(password)
        logger.info(f'Generated password: {password}')
        return password

    @classmethod
    def _insert_uppercase(cls, password):
        while True:
            index = random.randint(0, len(password) - 1)
            if password[index] not in string.ascii_letters:
                continue
            return password[:index] + password[index].upper() + password[index+1:]

    @classmethod
    def _insert_number(cls, password):
        while True:
            if any(char.isdigit() for char in password):
                return password
            index = random.randint(0, len(password) - 1)
            if password[index] not in string.ascii_letters or password.isupper():
                continue
            return password[:index] + str(random.randint(0, 9)) + password[index+1:]

    @classmethod
    def _insert_symbol(cls, password):
        while True:
            if any(char in string.punctuation for char in password):
                return password
            index = random.randint(0, len(password) - 1)
            if password[index] not in string.ascii_letters or password.isupper():
                continue
            return password[:index] + str(random.choice(string.punctuation)) + password[index+1:]

