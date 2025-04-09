from database import initialize_user_db, USER_DB, global_change_db
from auth import hash_password, check_password
from utils import is_valid_password
import csv

current_user = None


def set_username(username):
    """
    Sets the current signed-in user.

    Args:
        username (str): The username to set as the current user.

    Returns:
        str: Confirmation message of the user being set.

    """
    global current_user
    current_user = username
    return f"Username '{username}' is set."


def get_current_user():
    """
    Gets the current signed-in user.

    Returns:
        str: The username of the signed-in user, or a message indicating no user is signed in.

    """
    if current_user:
        return f"Current signed-in user: {current_user}"
    else:
        return "No user is signed in."


def sign_up(username, password):
    """
    Registers a new user in the system.

    Args:
        username (str): The username for the new user.
        password (str): The password for the new user.

    Returns:
        str: A success message or an error message if the username already exists or the password is invalid.
    """
    initialize_user_db()
    db_file = global_change_db()

    normalized_username = username.lower()

    try:
        is_valid_password(password)
    except ValueError as e:
        return str(e)

    with open(db_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'].lower() == normalized_username:
                return "Username already exists."

    hashed_password = hash_password(password)
    with open(db_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([normalized_username, hashed_password.decode('utf-8')])

    return "Sign up successful!"


def sign_in(username, password):
    """
    Signs in a user.

    Args:
        username (str): The username of the user.
        password (str): The password for the user.

    Returns:
        str: A success message, an error message if the user is already signed in, or if the credentials are invalid.
    """
    global current_user

    # Check if a user is already signed in
    if current_user is not None:
        return f"Error: User '{current_user}' is already signed in. Please sign out first."

    # Initialize the database and get its path
    initialize_user_db()
    db_file = global_change_db()

    # Validate the username and password
    with open(db_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                # Verify the password
                if check_password(row['password'].encode('utf-8'), password):
                    return set_username(username)
                else:
                    return "Invalid password."

    # If username is not found
    return "Username not found."


def sign_out():
    """
    Signs out the current user.

    Returns:
        str: A success message if a user is signed out, or an error message if no user is signed in.
    """
    global current_user
    if current_user is None:
        return "No user is signed in."

    user = current_user
    current_user = None
    return f"User '{user}' signed out successfully!"


def update_password(old_password, new_password):
    """
    Updates the password for the signed-in user.

    Args:
        old_password (str): The current password of the user.
        new_password (str): The new password to set.

    Returns:
        str: A success message if the password is updated, or an error message if not.

    """
    global current_user
    if current_user is None:
        return "No user is signed in."

    initialize_user_db()

    try:
        is_valid_password(new_password)
    except ValueError as e:
        return str(e)

    users = []
    password_updated = False
    db_file = global_change_db()

    with open(db_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == current_user:
                if check_password(row['password'].encode('utf-8'), old_password):
                    row['password'] = hash_password(
                        new_password).decode('utf-8')
                    password_updated = True
                else:
                    return "Old password is incorrect."
            users.append(row)

    if not password_updated:
        return "Error: Failed to update the password."

    with open(db_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password"])
        writer.writeheader()
        writer.writerows(users)

    return f"Password for user '{current_user}' updated successfully!"


def delete_user(username):
    """
    Deletes a user from the database.

    Args:
        username (str): The username of the user to delete.

    Returns:
        str: A success message if the user is deleted, or an error message if the user is not found.

    Examples:
        >>> USER_DB = "test_db.csv"
        >>> sign_up("john_doe", "Password123!")
        'Sign up successful!'
        >>> delete_user("john_doe")
        "User 'john_doe' deleted successfully!"
        >>> delete_user("jane_doe")
        'Username not found.'
    """
    initialize_user_db()
    db_file = global_change_db()
    users = []
    user_deleted = False

    with open(db_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                user_deleted = True
            else:
                users.append(row)

    if not user_deleted:
        return "Username not found."

    with open(db_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password"])
        writer.writeheader()
        writer.writerows(users)

    return f"User '{username}' deleted successfully!"
