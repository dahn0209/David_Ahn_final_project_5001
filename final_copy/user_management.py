from database import initialize_user_db, USER_DB, global_change_db
from auth import hash_password, check_password
from utils import is_valid_password
import csv

current_user = None


def set_username(username):

    global current_user
    current_user = username
    return f"Username '{username}' is set."


def get_current_user():

    if current_user:
        return f"Current signed-in user: {current_user}"
    else:
        return "No user is signed in."


def sign_up(username, password):
    # Ensure the user database is initialized before proceeding
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

    global current_user
    db_file = global_change_db() 
    if current_user is not None:
        return f"Error: User '{current_user}' is already signed in. Please sign out first."

    initialize_user_db()
    with open(db_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                if check_password(row['password'].encode('utf-8'), password):
                    return set_username(username)
                else:
                    return "Invalid password."
    return "Username not found."




def sign_out():

    global current_user
    if current_user is not None:
        user = current_user
        current_user = None
        return f"User '{user}' signed out successfully!"
    else:
        return "No user is signed in."


def update_password(old_password, new_password):

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
    db_file=global_change_db()

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

    initialize_user_db()
    db_file=global_change_db()
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
