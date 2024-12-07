import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from auth import hash_password, check_password


class TestAuth(unittest.TestCase):
    def test_hash_password(self):
        password = "StrongPass123!"
        hashed = hash_password(password)
        self.assertNotEqual(password, hashed)  # Ensure password is hashed
        self.assertTrue(len(hashed) > len(password))  # Ensure hashing

    def test_check_password(self):
        password = "StrongPass123!"
        hashed = hash_password(password)
        self.assertTrue(check_password(hashed, password))  # Valid password
        self.assertFalse(check_password(hashed, "WrongPassword"))  # Invalid password

if __name__ == '__main__':
    unittest.main()


