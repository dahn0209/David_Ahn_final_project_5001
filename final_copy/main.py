from database import (
    set_user_db,
    create_new_user_db,
    get_current_db,
    delete_user_db,
    initialize_user_db,
    USER_DB,
)
from user_management import (
    sign_up,
    sign_in,
    sign_out,
    update_password,
    delete_user,
    get_current_user,
)


def display():
    """
    Displays the main menu options to the user.

    Examples:
        >>> display()
        User System
        1. Set User Database
        2. Create New User Database
        3. View Current Database
        4. Sign Up
        5. Sign In
        6. Sign Out
        7. Update Password
        8. Delete User
        9. Delete User Database
        10. Get Current User
        11. Exit
    """
    print("User System")
    print("1. Set User Database")
    print("2. Create New User Database")
    print("3. View Current Database")
    print("4. Sign Up")
    print("5. Sign In")
    print("6. Sign Out")
    print("7. Update Password")
    print("8. Delete User")
    print("9. Delete User Database")
    print("10. Get Current User")
    print("11. Exit")


def choices(choice):
    """
    Handles the user's menu choice and executes the action.

    Args:
        choice (str): The menu option chosen by the user.

    Returns:
        bool: False if the user chooses to exit; True otherwise.

    Examples: # check test_main.py
        >>> choices("3")  # Assuming the current database is "user_db.csv"
        The current db is user_db.csv
        True
        >>> choices("11")
        Goodbye!
        False
        >>> choices("99")  # Invalid choice
        Invalid choice. Please try again.
        True
    """
    try:
        if choice == "1":
            new_db = input("Enter the existing CSV file to use: ")
            print(set_user_db(new_db))
        elif choice == "2":
            new_db_name = input("Enter the name of the new user database to create: ")
            print(create_new_user_db(new_db_name))
        elif choice == "3":
            print(get_current_db())
        elif choice == "4":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(sign_up(username, password))
        elif choice == "5":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(sign_in(username, password))
        elif choice == "6":
            print(sign_out())
        elif choice == "7":
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            print(update_password(old_password, new_password))
        elif choice == "8":
            username = input("Enter username to delete: ")
            print(delete_user(username))
        elif choice == "9":
            print(delete_user_db())
        elif choice == "10":
            print(get_current_user())
        elif choice == "11":
            print("Goodbye!")
            return False
        else:
            print("Invalid choice. Please try again.")
    except Exception as e:
        print(f"Error: {e}")
    return True


def main():
    """
    Main entry point for the user system. Displays a menu for the user to interact with
    the system and executes actions based on the user's choices.

    Examples:
        >>> main()  # Interactive session, cannot be tested directly.
    """
    initialize_user_db()
    running = True
    while running:
        display()
        choice = input("Choose an option: ")
        running = choices(choice)


if __name__ == "__main__":
    main()
