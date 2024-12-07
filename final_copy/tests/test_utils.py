import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import is_valid_password

class TestUtils(unittest.TestCase):
    def test_is_valid_password(self):
        with self.assertRaises(ValueError):
            is_valid_password("short")
        with self.assertRaises(ValueError):
            is_valid_password("NoSpecial123")
        self.assertTrue(is_valid_password("ValidPass123!"))

if __name__ == '__main__':
    unittest.main()
