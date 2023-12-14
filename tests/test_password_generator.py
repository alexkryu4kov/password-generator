import string
import unittest

from parameterized import parameterized

from app.main.password_generator import PasswordGenerator


class TestPasswordGenerator(unittest.TestCase):

    @parameterized.expand([
        (10, False, False, False),
        (10, True, False, False),
        (10, False, True, False),
        (10, False, False, True),
        (15, True, True, True)
    ])
    def test_generate_password_simple(self, length, uppercase, digits, symbols):
        password = PasswordGenerator.generate_password(length=length, uppercase=uppercase, digits=digits, symbols=symbols)
        self.assertEqual(len(password), length)
        self.assertEqual(any(char.isupper() for char in password), uppercase)
        self.assertEqual(any(char.isdigit() for char in password), digits)
        self.assertEqual(any(char in string.punctuation for char in password), symbols)
