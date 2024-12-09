from database import USER_DB
from main import choices
import unittest
from unittest.mock import patch, MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestChoicesFunction(unittest.TestCase):
    """
    Test case for testing the choices function in the main program.

    This class contains unit tests for the `choices` function, which handles 
    different user input options in the program. 

      to exit the program.
    - test_choice_99_invalid_option: Tests the behavior when an invalid 
      option (e.g., "99") is selected.
    """

    def setUp(self):
        """
        Sets up the test environment by setting the global USER_DB to a mock 
        database file ("user_db.csv") before each test.
        """
        global USER_DB
        USER_DB = "user_db.csv"

    @patch("builtins.input", side_effect=[""])
    @patch("builtins.print")
    def test_choice_3_view_current_db(self, mock_print, mock_input):
        """
        Tests the behavior when option "3" is selected to view the current 
        database.

        The test mocks user input and verifies the name of the current database (USER_DB)
        """
        result = choices("3")
        mock_print.assert_called_once_with(f"The current db is {USER_DB}")
        self.assertTrue(result)

    @patch("builtins.print")
    def test_choice_11_exit(self, mock_print):
        """
        Tests the behavior when option "11" is selected to exit the program.

        """
        result = choices("11")
        # Check if the exit message is printed
        mock_print.assert_called_once_with("Goodbye!")
        # Check that the result is False, indicating exit
        self.assertFalse(result)

    @patch("builtins.print")
    def test_choice_99_invalid_option(self, mock_print):
        """
        Tests the behavior when an invalid option is selected.

        """
        result = choices("99")
        # Check if the invalid option message is printed
        mock_print.assert_called_once_with("Invalid choice. Please try again.")
        # Check that the result is True, indicating the prompt continues
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
