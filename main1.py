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


def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\nUser System")
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


def handle_choice(choice):
    """
    Handles the user's menu choice.
    Args:
        choice (str): The menu option chosen by the user.
    """
    try:
        if choice == "1":
            new_db = input("Enter the existing CSV file to use: ")
            print(set_user_db(new_db))
        elif choice == "2":
            new_db_name = input(
                "Enter the name of the new user database to create: ")
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
            confirm = input(
                "Are you sure you want to delete the database? (yes/no): ")
            print(delete_user_db(confirm))
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
    Main entry point for the user system.
    """
    initialize_user_db()
    running = True
    while running:
        display_menu()
        choice = input("Choose an option: ")
        running = handle_choice(choice)


if __name__ == "__main__":
    main()
