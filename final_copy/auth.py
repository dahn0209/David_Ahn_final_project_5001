import bcrypt


def hash_password(password):
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The plaintext password to hash. 

    Returns:
        bytes: The hashed password as a byte string.

    Raises:
        ValueError: If the password is an empty string.

    Example:
        >>> hashed = hash_password("StrongPass123!")
        >>> isinstance(hashed, bytes)
        True
        >>> hashed.startswith(b"$2b$")
        True

        >>> hash_password("") 
        Traceback (most recent call last):
        ...
        ValueError: Password cannot be empty.

        >>> special_password = "!@#$%^&*()_+{}:<>?"
        >>> hashed = hash_password(special_password)
        >>> isinstance(hashed, bytes)
        True

        >>> long_password = "a" * 100  # 100 characters
        >>> hashed = hash_password(long_password)
        >>> isinstance(hashed, bytes)
        True

        >>> special_password = "!@#$%^&*()_+{}:<>?"
        >>> hashed = hash_password(special_password)
        >>> isinstance(hashed, bytes)
        True

        >>> unicode_password = "P@sswørd✨"
        >>> hashed = hash_password(unicode_password)
        >>> isinstance(hashed, bytes)
        True

        >>> password = "Repeated123!"
        >>> hash1 = hash_password(password)
        >>> hash2 = hash_password(password)
        >>> hash1 != hash2
        True
    """
    if not password:
        raise ValueError("Password cannot be empty.")

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def check_password(hashed_password, password):
    """
    Verifies whether a plaintext password matches a given bcrypt hashed password.

    Args:
        hashed_password (bytes): The hashed password to verify against.
                                 Must be a bcrypt-generated hash in byte format.
        password (str): The plaintext password to check.

    Returns:
        bool: `True` if the password matches the hashed password, `False` otherwise.

    Example:
        >>> from bcrypt import hashpw, gensalt
        >>> hashed = hashpw("MySecurePass!".encode('utf-8'), gensalt())
        >>> check_password(hashed, "MySecurePass!")
        True

        >>> check_password(hashed, "WrongPass")
        False

        >>> check_password(hashed, "")
        Traceback (most recent call last):
        ...
        ValueError: Password cannot be empty.

        >>> check_password(None, "password123")
        Traceback (most recent call last):
        ...
        TypeError: Hashed password cannot be None.

        >>> check_password(hashed, None)
        Traceback (most recent call last):
        ...
        TypeError: Password cannot be None.

    """
    if hashed_password is None:
        raise TypeError("Hashed password cannot be None.")
    if not isinstance(hashed_password, bytes):
        raise ValueError("Hashed password must be in byte format.")
    if password is None:
        raise TypeError("Password cannot be None.")
    if password == "":
        raise ValueError("Password cannot be empty.")

    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
