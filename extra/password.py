import bcrypt
import csv
import os
import re

# Default user database
USER_DB = "users_3.csv"

# Global variable to track the current user
current_user = None

# Set the user database file dynamically


def set_user_db(file_name):
    global USER_DB
    if not os.path.exists(file_name):
        return f"Error: The file '{file_name}' does not exist."
    USER_DB = file_name
    return f"User database set to '{file_name}'."

# Get current db


def get_current_db():
    return f"Current user database: '{USER_DB}'"

# Initialize the CSV file if it doesn't exist


def initialize_user_db():
    try:
        with open(USER_DB, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])  # Add a header
    except FileExistsError:
        pass  # File already exists

# Create a new user database


def create_new_user_db(new_db_name):
    if os.path.exists(new_db_name):
        return f"The file '{new_db_name}' already exists."
    with open(new_db_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password"])  # Add a header
    return f"New user database '{new_db_name}' created successfully."

# Delete the user database CSV file


def delete_user_db():
    if os.path.exists(USER_DB):
        confirmation = input(f"Are you sure you want to delete the database '{
                             USER_DB}'? This action cannot be undone. (yes/no): ")
        if confirmation.lower() == "yes":
            os.remove(USER_DB)
            return f"Database '{USER_DB}' has been deleted."
        else:
            return "Action canceled."
    else:
        return f"Database '{USER_DB}' does not exist."

# Hash the password using bcrypt


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pw

# Check if the password matches the hashed password


def check_password(hashed_password, password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)

# Set the current user after a successful sign-in


def set_username(username):
    global current_user
    current_user = username
    return f"Username '{username}' is now set."

# Get current signed-in user


def get_current_user():
    if current_user is not None:
        return f"Current signed-in user: {current_user}"
    else:
        return "No user is currently signed in."

# Sign up function (uses the current USER_DB file)


def sign_up(username, password):
    initialize_user_db()
    try:
        is_valid_password(password)
    except ValueError as e:
        return str(e)  # Return the error message if password is invalid

    with open(USER_DB, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return "Username already exists."

    hashed_password = hash_password(password)

    with open(USER_DB, 'a', newline='') as file:
        writer = csv.writer(file)
        # Store hashed password as string
        writer.writerow([username, hashed_password.decode('utf-8')])

    return "Sign up successful!"

# Validate password strength


def is_valid_password(password):
    if len(password) <= 8:
        raise ValueError("Password must be more than 8 characters.")
    if len(password) > 20:
        raise ValueError("Password must be less than 20 characters.")
    if not re.search(r"[a-z]", password):
        raise ValueError(
            "Password must contain at least one lowercase letter.")
    if not re.search(r"[A-Z]", password):
        raise ValueError(
            "Password must contain at least one uppercase letter.")
    if not re.search(r"[0-9]", password):
        raise ValueError("Password must contain at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValueError(
            "Password must contain at least one special character.")
    if re.search(r"\s", password):
        raise ValueError("Password must not contain spaces.")
    return True

# Sign in function (modified to check if a user is already signed in)


def sign_in(username, password):
    global current_user
    # Check if there's already a user signed in
    if current_user is not None:
        return f"Error: User '{current_user}' is already signed in. Please sign out first."

    initialize_user_db()
    with open(USER_DB, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                # Compare entered password with hashed password
                if check_password(row['password'].encode('utf-8'), password):
                    # Set the username after successful sign-in
                    return set_username(username)
                else:
                    return "Invalid password."
    return "Username not found."

# Sign out function


def sign_out():
    global current_user
    if current_user is not None:
        user = current_user
        current_user = None
        return f"User '{user}' signed out successfully!"
    else:
        return "No user is currently signed in."

# Update password function


def update_password(username, old_password, new_password):
    initialize_user_db()
    try:
        is_valid_password(new_password)  # Validate the new password
    except ValueError as e:
        # Return the error message if the new password is invalid
        return str(e)

    users = []
    password_updated = False

    with open(USER_DB, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                # Check old password against hashed password
                if check_password(row['password'].encode('utf-8'), old_password):
                    row['password'] = hash_password(
                        new_password).decode('utf-8')
                    password_updated = True
                else:
                    return "Old password is incorrect."
            users.append(row)

    if not password_updated:
        return "Username not found."

    with open(USER_DB, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["username", "password"])
        writer.writeheader()
        writer.writerows(users)

    return "Password updated successfully!"

# Delete a user


def delete_user(username):
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


if __name__ == "__main__":
    initialize_user_db()
    while True:
        print("\nUser Management System")
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
        choice = input("Choose an option: ")

        if choice == "1":
            new_db = input("Enter the name of an existing CSV file to use: ")
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
            username = input("Enter username: ")
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            print(update_password(username, old_password, new_password))
        elif choice == "8":
            username = input("Enter username to delete: ")
            print(delete_user(username))
        elif choice == "9":
            print(delete_user_db())
        elif choice == "10":
            print(get_current_user())
        elif choice == "11":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
