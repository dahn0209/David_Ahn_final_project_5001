from database import delete_user_db, USER_DB
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestDeleteUserDb(unittest.TestCase):
    """
    Test case for the delete_user_db function.

    """

    def setUp(self):
        """
        Sets up the test environment by creating a temporary user database file 
        with a header row ("username,password").
        """
        with open(USER_DB, "w") as f:
            f.write("username,password\n")

    def tearDown(self):
        """
        Cleans up after each test by removing the user database file if it 
        exists. Ensures a clean state for the next test.
        """
        if os.path.exists(USER_DB):
            os.remove(USER_DB)

    def test_delete_existing_db(self):
        """
        Tests the delete_user_db function when the database file exists.

        """
        self.assertTrue(os.path.exists(USER_DB))
        result = delete_user_db()
        self.assertEqual(result, f"Database '{USER_DB}' has been deleted.")
        self.assertFalse(os.path.exists(USER_DB))

    def test_delete_nonexistent_db(self):
        """
        Tests the delete_user_db function when the database file does not exist.

        """
        if os.path.exists(USER_DB):
            os.remove(USER_DB)
        self.assertFalse(os.path.exists(USER_DB))
        result = delete_user_db()
        self.assertEqual(result, f"Database '{USER_DB}' does not exist.")


if __name__ == "__main__":
    unittest.main()
