import os
import csv

USER_DB = "user_db.csv"


def set_user_db(file_name):
    """
    Sets the user database to the specified file.

    Parameters:
        file_name (str): The name of the database file to use.

    Returns:
        str: A message indicating whether the database file was set successfully
             or if the specified file does not exist.

    Edge Cases:
        >>> set_user_db("new_user_db.csv")
        "Error: The file 'new_user_db.csv' does not exist."

        >>> set_user_db("existing_db.csv")
        "User database set to 'existing_db.csv'."
    """

    global USER_DB
    if not os.path.exists(file_name):
        return f"Error: The file '{file_name}' does not exist."
    USER_DB = file_name
    return f"User database set to '{file_name}'."


def get_current_db():
    """
    Retrieves the name of the current user database file.

    Returns:
        str: The name of the file currently set as the user database.

    Edge Cases:
        - `USER_DB` has not been initialized (should still return the default value).

    Examples:
        >>> get_current_db()
        "Current user database: 'user_db.csv'"
    """

    return f"Current user database: '{USER_DB}'"


def initialize_user_db():
    """
    Initializes the user database by creating the file if it does not already exist.

    Parameters:
        None

    Returns:
        None

    Edge Cases:
        >>> initialize_user_db()
        # Creates the `user_db.csv` file if it does not exist.
    """
    try:
        with open(USER_DB, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])
    except FileExistsError:
        pass


def create_new_user_db(new_db_name):
    """
    Creates a new user database file with the required headers.

    Parameters:
        new_db_name (str): The name of the new database file to create.

    Returns:
        str: A message indicating whether the new database file was created successfully
             or if it already exists.

    Edge Cases:
        >>> create_new_user_db("new_user_db.csv")
        "New user database 'new_user_db.csv' created successfully."

        >>> create_new_user_db("existing_db.csv")
        "The file 'existing_db.csv' already exists."
    """


    if os.path.exists(new_db_name):
        return f"The file '{new_db_name}' already exists."
    with open(new_db_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password"])
    return f"New user database '{new_db_name}' created successfully."


def delete_user_db():
    """
    Deletes the current user database file.

    Parameters:
        None

    Returns:
        str: A message indicating whether the database was deleted, canceled,
             or if the file does not exist.

    Edge Cases:
        >>> delete_user_db()
        "Are you sure you want to delete the database 'user_db.csv'? (yes/no): yes"
        "Database 'user_db.csv' has been deleted."
        >>> delete_user_db()
        "Are you sure you want to delete the database 'user_db.csv'? (yes/no): no"
        "Canceled!"
        >>> delete_user_db()
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
