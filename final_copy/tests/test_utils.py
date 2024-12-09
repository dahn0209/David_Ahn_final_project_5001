import unittest
from unittest.mock import patch, mock_open
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import is_valid_password, is_password_reused
import bcrypt


class TestPasswordValidation(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data="username,password\nuser1,password123!"))
    @patch("bcrypt.checkpw")
    def test_valid_password(self, mock_checkpw):
        """
        Test case for a valid password.
        """
        # Mock bcrypt to return False for password match
        mock_checkpw.return_value = False
        password = "Valid1Password!"
        self.assertTrue(is_valid_password(password))

    def test_password_too_short(self):
        """
        Test case for a password that is less than 8 characters.
        """
        password = "Short1!"
        with self.assertRaises(ValueError) as context:
            is_valid_password(password)
        self.assertEqual(str(context.exception), "Password must be more than 8 characters.")

    def test_password_too_long(self):
        """
        Test case for a password that is greater than 20 characters.
        """
        password = "ThisIsAVeryLongPasswordHERE123!"
        with self.assertRaises(ValueError) as context:
            is_valid_password(password)
        self.assertEqual(str(context.exception), "Password must be less than 20 characters.")

    def test_missing_lowercase(self):
        """
        Test case for a password that is missing a lowercase letter.
        """
        password = "PASSWORD123!"
        with self.assertRaises(ValueError) as context:
            is_valid_password(password)
        self.assertEqual(str(context.exception), "Password must contain at least one lowercase letter.")

    def test_missing_uppercase(self):
        """
        Test case for a password that is missing an uppercase letter.
        """
        password = "password123!"
        with self.assertRaises(ValueError) as context:
            is_valid_password(password)
        self.assertEqual(str(context.exception), "Password must contain at least one uppercase letter.")

    def test_missing_digit(self):
        """
        Test case for a password that is missing a digit.
        
        """
        password = "Password!"
        with self.assertRaises(ValueError) as context:
            is_valid_password(password)
        self.assertEqual(str(context.exception), "Password must contain at least one number.")

    def test_missing_special_char(self):
        """
        Test case for a password that is missing a special character.
        """
        password = "Password123"
        with self.assertRaises(ValueError) as context:
            is_valid_password(password)
        self.assertEqual(str(context.exception), "Password must contain at least one special character.")

    def test_password_with_spaces(self):
        """
        Test case for a password that contains spaces.
        """
        password = "Password 123!"
        with self.assertRaises(ValueError) as context:
            is_valid_password(password)
        self.assertEqual(str(context.exception), "Password must not contain spaces.")

    @patch("builtins.open", mock_open(read_data="username,password\nuser1,password123!\nuser2,Valid1Password!"))
    @patch("bcrypt.checkpw")
    def test_reused_password(self, mock_checkpw):
        """
        Test case for a reused password.
        """
        mock_checkpw.return_value = True
        password = "Valid1Password!"
        with self.assertRaises(ValueError) as context:
            is_valid_password(password)
        self.assertEqual(str(context.exception), "Password is already in use by another account.")

    @patch("builtins.open", mock_open(read_data="username,password\nuser1,newPassword123!"))
    @patch("bcrypt.checkpw")
    def test_non_reused_password(self, mock_checkpw):
        """
        Test case for a non-reused password.
        """
        mock_checkpw.return_value = False
        password = "NewValidPassword123!"
        self.assertTrue(is_valid_password(password))


if __name__ == '__main__':
    unittest.main()
