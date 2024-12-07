from database import initialize_user_db, USER_DB
from auth import hash_password, check_password
from utils import is_valid_password
import csv

current_user = None


def set_username(username):
    """
    Sets the current signed-in user's username.

    This function is used to track the username of the currently signed-in user globally.

    Parameters:
        username (str): The username to set as the current user.

    Returns:
        str: A confirmation message indicating that the username is set.

    Edge Cases:
        >>> set_username("JohnDoe")
        "Username 'JohnDoe' is set."
    """
    global current_user
    current_user = username
    return f"Username '{username}' is set."


def get_current_user():
    """
    Retrieves the currently signed-in user's username.

    Returns:
        str: The username of the current signed-in user, or a message indicating no user is signed in.

    Edge Cases:
        >>> get_current_user()
        "No user is signed in."

        >>> set_username("JaneDoe")
        >>> get_current_user()
        "Current signed-in user: JaneDoe"
    """

    return f"Current signed-in user: {current_user}" if current_user else "No user is signed in."


def sign_up(username, password):
    """
    Registers a new user with a username and password.


    Parameters:
        username (str): The desired username for the new user.
        password (str): The desired password for the new user.

    Returns:
        str: A success message if the user is registered, or an error message if the username already exists
             or the password is invalid.

    Edge Cases:
        >>> sign_up("JohnDoe", "SecureP@ssw0rd")
        "Sign up successful!"

        >>> sign_up("JohnDoe", "weakpass")
        "Password must contain at least one special character."

        >>> sign_up("johndoe", "SecureP@ssw0rd")
        "Username already exists."
    """

    initialize_user_db()
    normalized_username = username.lower()
    try:
        is_valid_password(password)
    except ValueError as e:
        return str(e)
    with open(USER_DB, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'].lower() == normalized_username:
                return "Username already exists."

    hashed_password = hash_password(password)

    with open(USER_DB, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([normalized_username, hashed_password.decode('utf-8')])

    return "Sign up successful!"


def sign_in(username, password):
    """
    Signs in a user if the username and password match an entry in the database.

    Parameters:
        username (str): The username of the user attempting to sign in.
        password (str): The plaintext password provided by the user.

    Returns:
        str: A message indicating the result of the sign-in attempt.

    Edge Cases:
        >>> sign_in("JohnDoe", "SecureP@ssw0rd")
        "Username 'JohnDoe' is set."

        >>> sign_in("JohnDoe", "WrongPassword")
        "Invalid password."

        >>> sign_in("NonExistentUser", "SecureP@ssw0rd")
        "Username not found."
    """

    global current_user
    if current_user is not None:
        return f"Error: User '{current_user}' is already signed in. Please sign out first."

    initialize_user_db()
    with open(USER_DB, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                if check_password(row['password'].encode('utf-8'), password):
                    return set_username(username)
                else:
                    return "Invalid password."
    return "Username not found."


def sign_out():
    """
    Signs out the currently signed-in user.

    Returns:
        str: A message indicating the result of the sign-out attempt.

    Edge Cases:
        >>> sign_out()
        "No user is signed in."

        >>> set_username("JohnDoe")
        >>> sign_out()
        "User 'JohnDoe' signed out successfully!"
    """

    global current_user
    if current_user is not None:
        user = current_user
        current_user = None
        return f"User '{user}' signed out successfully!"
    else:
        return "No user is signed in."


def update_password(old_password, new_password):
    """
    Updates the password of the currently signed-in user.

    Parameters:
        old_password (str): The current password of the user.
        new_password (str): The new password to replace the old one.

    Returns:
        str: A message indicating the result of the password update.

    Edge Cases:
        >>> set_username("JohnDoe")
        >>> update_password("OldP@ssw0rd", "NewSecureP@ss")
        "Password for user 'JohnDoe' updated successfully!"

        >>> update_password("WrongOldPassword", "NewSecureP@ss")
        "Old password is incorrect."
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

    with open(USER_DB, 'r') as file:
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

    with open(USER_DB, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password"])
        writer.writeheader()
        writer.writerows(users)

    return f"Password for user '{current_user}' updated successfully!"


def delete_user(username):
    """
    Deletes a user account from the database.


    Parameters:
        username (str): The username of the account to delete.

    Returns:
        str: A message indicating the result of the deletion attempt.

    Edge Cases:
        >>> delete_user("JohnDoe")
        "User 'JohnDoe' deleted successfully!"

        >>> delete_user("NonExistentUser")
        "Username not found."
    """

    initialize_user_db()
    users = []
    user_deleted = False

    with open(USER_DB, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                user_deleted = True
            else:
                users.append(row)

    if not user_deleted:
        return "Username not found."

    with open(USER_DB, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password"])
        writer.writeheader()
        writer.writerows(users)

    return f"User '{username}' deleted successfully!"
