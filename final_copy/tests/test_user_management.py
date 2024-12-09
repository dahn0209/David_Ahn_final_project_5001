import unittest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from user_management import (
    set_username, get_current_user, sign_up, sign_in, sign_out,
    update_password, delete_user, current_user
)
from database import initialize_user_db, global_change_db


class TestUserManagement(unittest.TestCase):
    """

    This class contains test cases that verify user authentication and 
    management operations such as sign up, sign in, sign out, update password, 
    and delete user.

   
    """

    def setUp(self):
        """
        Prepares the test environment by resetting global variables and 
        initializing the user database before each test.
        """
        global current_user
        current_user = None  # Ensures no user is signed in before each test
        global_change_db()  # Switch to test database
        initialize_user_db()  # Initialize a fresh database for each test

    def tearDown(self):
        """
        Cleans up after each test case by removing the test database 
        to ensure no interference between tests.
        """
        db_file = global_change_db()
        if os.path.exists(db_file):
            os.remove(db_file)  # Delete the test database after each test

    def test_set_username(self):
        """
        Tests setting a username successfully.

        """
        result = set_username("john_doe")
        self.assertEqual(result, "Username 'john_doe' is set.")

    def test_get_current_user_signed_in(self):
        """
        Tests retrieving the current signed-in user when a user is logged in.

        """
        set_username("john_doe")
        result = get_current_user()
        self.assertEqual(result, "Current signed-in user: john_doe")

    def test_get_current_user_not_signed_in(self):
        """
        Tests retrieving the current signed-in user when no user is logged in.

        """
        result = get_current_user()
        self.assertEqual(result, "No user is signed in.")

    def test_sign_in_success(self):
        """
        Tests successful sign-in with correct credentials.

        """
        sign_up("john_doe", "Password123!")
        sign_out()  # Ensure no user is signed in before testing
        result = sign_in("john_doe", "Password123!")
        self.assertEqual(result, "Username 'john_doe' is set.")

    def test_sign_up_existing_user(self):
        """
        Tests signing up with an already existing username.

        """
        sign_up("john_doe", "Password123!")
        result = sign_up("john_doe", "AnotherPassword123!")
        self.assertEqual(result, "Username already exists.")

    def test_sign_up_invalid_password(self):
        """
        Tests signing up with an invalid password.

        """
        result = sign_up("john_doe", "short")
        self.assertEqual(result, "Password must be more than 8 characters.")

    def test_sign_in_invalid_password(self):
        """
        Tests sign-in with an incorrect password.

        """
        sign_up("john_doe", "Password123!")
        sign_out()
        result = sign_in("john_doe", "WrongPassword!")
        self.assertEqual(result, "Invalid password.")

    def test_sign_in_user_not_found(self):
        """
        Tests sign-in with a non-existent username.

        """
        sign_out()
        result = sign_in("nonexistent_user", "Password123!")
        self.assertEqual(result, "Username not found.")

    def test_sign_in_user_already_signed_in(self):
        """
        Tests attempting to sign in with a different user while already signed in.

        """
        sign_up("john_doe", "Password123!")
        sign_in("john_doe", "Password123!")
        result = sign_in("jane_doe", "Password123!")
        self.assertEqual(
            result, "Error: User 'john_doe' is already signed in. Please sign out first.")

    def test_sign_out_success(self):
        """
        Tests successful sign-out when a user is signed in.

        """
        sign_up("john_doe", "Password123!")
        sign_in("john_doe", "Password123!")
        result = sign_out()
        self.assertEqual(result, "User 'john_doe' signed out successfully!")

    def test_sign_out_no_user(self):
        """
        Tests sign-out when no user is signed in.

        """
        result = sign_out()
        self.assertEqual(result, "No user is signed in.")

    def test_update_password_success(self):
        """
        Tests successful password update.

        """
        sign_up("john_doe", "Password123!")
        sign_in("john_doe", "Password123!")
        result = update_password("Password123!", "NewPassword123!")
        self.assertEqual(
            result, "Password for user 'john_doe' updated successfully!")

    def test_update_password_wrong_old_password(self):
        """
        Tests attempting to update the password with an incorrect old password.

        """
        sign_up("john_doe", "Password123!")
        sign_in("john_doe", "Password123!")
        result = update_password("WrongPassword", "NewPassword123!")
        self.assertEqual(result, "Old password is incorrect.")

    def test_update_password_not_signed_in(self):
        """
        Tests attempting to update the password when no user is signed in.

        """
        result = update_password("Password123!", "NewPassword123!")
        self.assertEqual(result, "No user is signed in.")

    def test_delete_user_success(self):
        """
        Tests successful user deletion.

        """
        sign_up("john_doe", "Password123!")
        result = delete_user("john_doe")
        self.assertEqual(result, "User 'john_doe' deleted successfully!")

    def test_delete_user_not_found(self):
        """
        Tests attempting to delete a non-existent user.

        """
        result = delete_user("unknown_user")
        self.assertEqual(result, "Username not found.")


if __name__ == '__main__':
    unittest.main()
