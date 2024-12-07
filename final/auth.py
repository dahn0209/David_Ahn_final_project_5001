import bcrypt


def hash_password(password):
    """
    Hashes a plain text password using bcrypt .

    Parameters:
        password (str): The plain text password.

    Returns:
        bytes: The hashed password as a byte string.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def check_password(hashed_password, password):
    """
    Verifies a password against a previously hashed password.

    This function uses bcrypt to compare a plain-text password with a hashed password
    to determine if they match.

    Parameters:
        hashed_password (bytes): The bcrypt-hashed password stored in the database.
        password (str): The plain-text password to verify.

    Returns:
        bool: `True` if the password matches the hash; `False` otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
