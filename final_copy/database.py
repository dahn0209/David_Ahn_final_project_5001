import os
import csv

USER_DB = "user_db.csv"


def set_user_db(file_name):
    """
    Sets the global user database file to the specified file.

    Args:
        file_name (str): The name of the database file.

    Returns:
        str: Confirmation message or error if the file doesn't exist.

    Examples:
        >>> set_user_db("tests/existing_db.csv")  # Assuming the file exists
        "User database set to 'tests/existing_db.csv'."
        >>> set_user_db("nonexistent_file.csv")
        "Error: The file 'nonexistent_file.csv' does not exist."
    """
    global USER_DB
    if not os.path.exists(file_name):
        return f"Error: The file '{file_name}' does not exist."
    USER_DB = file_name
    return f"User database set to '{file_name}'."


def get_current_db():
    """
    Retrieves the name of the current database in use.

    Returns:
        str: The current database file.

    Examples:
        >>> get_current_db()
        'The current db is user_db.csv'
    """
    return f"The current db is {USER_DB}"


def global_change_db():
    """
    Retrieves the name of the current database (global USER_DB).

    Returns:
        str: The current database file.

    Examples:
        >>> global_change_db()
        'user_db.csv'
    """
    return USER_DB


def initialize_user_db():
    """
    Initializes the user database. Creates the database file if it doesn't exist.

    Examples:
        >>> initialize_user_db()  # Assuming 'user_db.csv' does not exist
        >>> os.path.exists('user_db.csv')
        True
    """
    db_file = global_change_db()
    if not os.path.exists(db_file):
        with open(db_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])


def create_new_user_db(new_db_name):
    """
    Creates a new user database with the specified name.

    Args:
        new_db_name (str): The name of the new database file.

    Returns:
        str: Confirmation message or error if the file already exists.

    Examples:
        >>> create_new_user_db("tests/new_db.csv")  #assuming new_db.csv is not in file
        "New database 'tests/new_db.csv' created."
        >>> create_new_user_db("tests/existing_db.csv")  
        "The file 'tests/existing_db.csv' already exists."
    """
    if os.path.exists(new_db_name):
        return f"The file '{new_db_name}' already exists."
    with open(new_db_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password"])
    return f"New database '{new_db_name}' created."


def delete_user_db():
    """
    Deletes the current user database file if it exists.

    Returns:
        str: Confirmation message or error if the file doesn't exist.

    Examples:  # Check test_database for accurate testing 
        >>> delete_user_db()  # Assuming 'user_db.csv' exists
        "Database 'user_db.csv' has been deleted."
        >>> delete_user_db()  # Assuming 'user_db.csv' does not exist
        "Database 'user_db.csv' does not exist."
    """
    if os.path.exists(USER_DB):
        confirmation = input(f"Are you sure you want to delete the database '{
                             USER_DB}'? (yes/no): ")
        if confirmation.lower() == "yes":
            os.remove(USER_DB)
            return f"Database '{USER_DB}' has been deleted."
        else:
            return "Canceled!"
    else:
        return f"Database '{USER_DB}' does not exist."
