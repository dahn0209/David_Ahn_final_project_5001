import os
import csv

USER_DB = "user_db.csv"

def set_user_db(file_name):
    """
    Sets the global user database file.
    
    Args:
        file_name (str): The file name to set as the user database.
    
    Returns:
        str: Success or error message.
    """
    global USER_DB
    if not os.path.exists(file_name):
        return f"Error: The file '{file_name}' does not exist."
    USER_DB = file_name
    return f"User database set to '{file_name}'."

def get_current_db():
    """
    Retrieves the current user database file.
    
    Returns:
        str: The name of the current database file.
    """
    return f"The current db is {USER_DB}"

def initialize_user_db():
    """
    Initializes the user database by creating a new file with default headers if it doesn't exist.
    """
    global USER_DB
    print('let look db initialize->',USER_DB)
    if not os.path.exists(USER_DB):
        _create_user_db(USER_DB)

def create_new_user_db(new_db_name):
    """
    Creates a new user database with the given name.
    
    Args:
        new_db_name (str): The name of the new database file.
    
    Returns:
        str: Success or error message.
    """
    if os.path.exists(new_db_name):
        return f"The file '{new_db_name}' already exists."
    _create_user_db(new_db_name)
    return f"New database '{new_db_name}' created."

def delete_user_db(confirm="no"):
    """
    Deletes the current user database file after confirmation.
    
    Args:
        confirm (str): Confirmation to delete ('yes' or 'no').
    
    Returns:
        str: Success or cancellation message.
    """
    if os.path.exists(USER_DB):
        if confirm.lower() == "yes":
            os.remove(USER_DB)
            return f"Database '{USER_DB}' has been deleted."
        else:
            return "Canceled!"
    return f"Database '{USER_DB}' does not exist."

# Helper function
def _create_user_db(file_name):
    """
    Creates a user database file with default headers.
    
    Args:
        file_name (str): The name of the file to create.
    """
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])  # Write the headers
    except Exception as e:
        raise IOError(f"Failed to create the database '{file_name}': {e}")
