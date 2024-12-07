import re
from auth import check_password
from database import USER_DB
import csv

def is_valid_password(password):

    if len(password) <= 8:
        raise ValueError("Password must be more than 8 characters.")
    if len(password) > 20:
        raise ValueError("Password must be less than 20 characters.")
    if not re.search(r"[a-z]", password):
        raise ValueError("Password must contain at least one lowercase letter.")
    if not re.search(r"[A-Z]", password):
        raise ValueError("Password must contain at least one uppercase letter.")
    if not re.search(r"[0-9]", password):
        raise ValueError("Password must contain at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        raise ValueError("Password must contain at least one special character.")
    if re.search(r"\s", password):
        raise ValueError("Password must not contain spaces.")

    if is_password_reused(password):
        raise ValueError("Password is already in use by another account.")

    return True



def is_password_reused(password):

    with open(USER_DB, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if check_password(row['password'].encode('utf-8'), password):
                return True
    return False