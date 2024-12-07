import bcrypt

def hash_password(password):
    """
    Hashes a plaintext password using bcrypt.

    Args:
        password (str): The plaintext password to hash. 
                        Must be a non-empty string.

    Returns:
        bytes: The hashed password as a byte string.

    Raises:
        ValueError: If the password is an empty string.

    Example:
        >>> hash_password("StrongPass123!")
        b'$2b$12$...' (The hashed password in bytes)

        >>> special_password = "!@#$%^&*()_+{}:<>?"
        >>> hashed = hash_password(special_password)
        >>> isinstance(hashed, bytes)
        True
        (Special characters are handled correctly and produce a valid bcrypt hash)

    Edge Cases and Results:
        1. Empty Password:
           >>> hash_password("")  # Raises ValueError
           Traceback (most recent call last):
               ...
           ValueError: Password cannot be empty.

        2. Very Long Password (exceeding bcrypt's 72-byte limit):
           >>> long_password = "a" * 100  # 100 characters
           >>> hashed = hash_password(long_password)
           >>> isinstance(hashed, bytes)
           True
           (bcrypt internally truncates passwords to 72 bytes before hashing)

        3. Special Characters in Password:
           >>> special_password = "!@#$%^&*()_+{}:<>?"
           >>> hashed = hash_password(special_password)
           >>> isinstance(hashed, bytes)
           True
           (Special characters are handled correctly and produce a valid bcrypt hash)

        4. Unicode Characters in Password:
           >>> unicode_password = "P@sswørd✨"
           >>> hashed = hash_password(unicode_password)
           >>> isinstance(hashed, bytes)
           True
           (Unicode characters are supported because they are encoded as UTF-8 before hashing)

        5. Repeated Hashing:
           >>> password = "Repeated123!"
           >>> hash1 = hash_password(password)
           >>> hash2 = hash_password(password)
           >>> hash1 != hash2
           True
           (bcrypt generates a unique salt for each hashing, so hashes for the same input differ)

    Notes:
        - The returned hash includes the salt, making it self-contained for verification later.
        - Bcrypt's truncation of passwords longer than 72 bytes means only the first 72 bytes are considered.

    """
    if not password:
        raise ValueError("Password cannot be empty.")

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

    if not password:
        raise ValueError("Password cannot be empty.")

    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)



def check_password(hashed_password, password):

    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
