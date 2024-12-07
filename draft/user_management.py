import csv
from database import initialize_user_db, USER_DB
from auth import hash_password, check_password
from utils import is_valid_password

current_user = None

def set_username(username):
    """
    Sets the current signed-in user.
    
    Args:
        username (str): The username to set as the current user.
    
    Returns:
        str: Confirmation message.
    """
    global current_user
    current_user = username
    return f"Username '{username}' is set."


def get_current_user():
    """
    Gets the current signed-in user.
    
    Returns:
        str: The current user or a message if no user is signed in.
    """
    return f"Current signed-in user: {current_user}" if current_user else "No user is signed in."


def _read_user_db():
    """
    Reads the user database into a list of dictionaries.
    
    Returns:
        list: A list of dictionaries representing users.
    """
    try:
        with open(USER_DB, 'r') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        return []
    except Exception as e:
        raise IOError(f"Error reading the user database: {e}")


def _write_user_db(users):
    """
    Writes the list of users to the database.
    
    Args:
        users (list): A list of dictionaries representing users.
    """
    try:
        with open(USER_DB, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["username", "password"])
            writer.writeheader()
            writer.writerows(users)
    except Exception as e:
        raise IOError(f"Error writing to the user database: {e}")


def sign_up(username, password):
    """
    Registers a new user with a hashed password.
    
    Args:
        username (str): The username to register.
        password (str): The password to hash and store.
    
    Returns:
        str: Success or error message.
    """
    if not username or not password:
        return "Error: Username and password cannot be empty."
    
    print('before sign up global DB->',USER_DB)
    initialize_user_db()
    print('sign up global DB->',USER_DB)
    users = _read_user_db()
    normalized_username = username.lower()

    if any(user['username'].lower() == normalized_username for user in users):
        return "Username already exists."

    try:
        is_valid_password(password)
        hashed_password = hash_password(password).decode('utf-8')
        users.append({"username": normalized_username, "password": hashed_password})
        _write_user_db(users)
        return "Sign up successful!"
    except ValueError as e:
        return str(e)


def sign_in(username, password):
    """
    Signs in a user if the credentials match.
    
    Args:
        username (str): The username to authenticate.
        password (str): The plain-text password to verify.
    
    Returns:
        str: Success or error message.
    """
    global current_user
    if current_user:
        return f"Error: User '{current_user}' is already signed in. Please sign out first."

    initialize_user_db()
    users = _read_user_db()
    for user in users:
        if user['username'] == username and check_password(user['password'].encode('utf-8'), password):
            return set_username(username)

    return "Invalid username or password."


def sign_out():
    """
    Signs out the current user.
    
    Returns:
        str: Success or error message.
    """
    global current_user
    if not current_user:
        return "No user is signed in."
    user = current_user
    current_user = None
    return f"User '{user}' signed out successfully!"


def update_password(old_password, new_password):
    """
    Updates the password for the signed-in user.
    
    Args:
        old_password (str): The current password.
        new_password (str): The new password to set.
    
    Returns:
        str: Success or error message.
    """
    global current_user
    if not current_user:
        return "No user is signed in."

    initialize_user_db()
    users = _read_user_db()

    for user in users:
        if user['username'] == current_user:
            if not check_password(user['password'].encode('utf-8'), old_password):
                return "Old password is incorrect."
            try:
                is_valid_password(new_password)
                user['password'] = hash_password(new_password).decode('utf-8')
                _write_user_db(users)
                return f"Password for user '{current_user}' updated successfully!"
            except ValueError as e:
                return str(e)

    return "Error: Failed to update the password."


def delete_user(username):
    """
    Deletes a user from the database.
    
    Args:
        username (str): The username to delete.
    
    Returns:
        str: Success or error message.
    """
    initialize_user_db()
    users = _read_user_db()
    updated_users = [user for user in users if user['username'] != username]

    if len(users) == len(updated_users):
        return "Username not found."

    _write_user_db(updated_users)
    return f"User '{username}' deleted successfully!"
