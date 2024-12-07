import unittest
from unittest.mock import patch, MagicMock
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from final_copy.main import main

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=['username1', 'StrongPass123!'])
    @patch('builtins.print')
    def test_user_signup(self, mock_print, mock_input):
        result = main.sign_up_user()
        mock_print.assert_any_call("Sign up successful!")
        self.assertEqual(result, "Sign up successful!")

    @patch('builtins.input', side_effect=['username1', 'WrongPass123'])
    @patch('builtins.print')
    def test_user_signin_invalid_password(self, mock_print, mock_input):
        result = main.sign_in_user()
        mock_print.assert_any_call("Invalid username or password.")
        self.assertEqual(result, "Invalid username or password.")

    @patch('builtins.input', side_effect=['username1', 'StrongPass123!'])
    @patch('builtins.print')
    def test_user_signin_success(self, mock_print, mock_input):
        result = main.sign_in_user()
        mock_print.assert_any_call("Welcome, username1!")
        self.assertEqual(result, "Welcome, username1!")

if __name__ == '__main__':
    unittest.main()
