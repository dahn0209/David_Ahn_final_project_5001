import os
import csv

USER_DB = "user_db.csv"


def set_user_db(file_name):

    global USER_DB
    if not os.path.exists(file_name):
        return f"Error: The file '{file_name}' does not exist."
    USER_DB = file_name
    return f"User database set to '{file_name}'."


def get_current_db():

    return f"The current db is {USER_DB}"


def global_change_db():

    return USER_DB


def initialize_user_db():
    db_file = global_change_db()
    if not os.path.exists(db_file):
        with open(db_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password"])  # Write the headers


def create_new_user_db(new_db_name):

    if os.path.exists(new_db_name):
        return f"The file '{new_db_name}' already exists."
    with open(new_db_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["username", "password"])
    return f"New  database '{new_db_name}' created."


def delete_user_db():

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
