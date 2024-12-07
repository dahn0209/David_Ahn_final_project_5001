import bcrypt

def hash_password(password):
    """
    Hashes a password using bcrypt.
    
    Args:
        password (str): The password to be hashed.
    
    Returns:
        bytes: The hashed password.
    
    Raises:
        ValueError: If the password is empty.
    """
    if not password:
        raise ValueError("Password cannot be empty.")

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def check_password(hashed_password, password):
    """
    Checks if a given password matches the hashed password.
    
    Args:
        hashed_password (bytes): The hashed password.
        password (str): The plain-text password to check.
    
    Returns:
        bool: True if the password matches, False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
