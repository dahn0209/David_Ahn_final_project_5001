import unittest
import os
import tempfile
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import set_user_db, get_current_db, create_new_user_db, initialize_user_db, delete_user_db



class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.temp_db = tempfile.NamedTemporaryFile(delete=False)
        self.temp_db.close()
        set_user_db(self.temp_db.name)

    def tearDown(self):
        if os.path.exists(self.temp_db.name):
            os.remove(self.temp_db.name)

    def test_set_user_db(self):
        result = set_user_db(self.temp_db.name)
        self.assertEqual(result, f"User database set to '{self.temp_db.name}'")
        self.assertEqual(get_current_db(), f"The current db is {self.temp_db.name}")

    def test_create_new_user_db(self):
        new_db = "test_new_db.csv"
        result = create_new_user_db(new_db)
        self.assertEqual(result, f"New  database '{new_db}' created.")
        self.assertTrue(os.path.exists(new_db))
        os.remove(new_db)

    def test_initialize_user_db(self):
        initialize_user_db()
        with open(self.temp_db.name, 'r') as file:
            headers = file.readline().strip()
        self.assertEqual(headers, "username,password")

    def test_delete_user_db(self):
        result = delete_user_db()
        self.assertIn("has been deleted", result)
        self.assertFalse(os.path.exists(self.temp_db.name))

if __name__ == '__main__':
    unittest.main()
