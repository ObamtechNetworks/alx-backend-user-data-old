#!/usr/bin/env python3
"""Password encryption"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hashes a password using bcrypt with a salt.

    Args:
        password (str): The password to hash.

    Returns:
        bytes: The hashed password as a byte string.
    """
    # Generate a salt
    salt = bcrypt.gensalt()
    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates that the provided password matches the hashed password.

    Args:
        hashed_password (bytes): The hashed password.
        password (str): The password to validate.

    Returns:
        bool: True if the password matches the hashed password,
        False otherwise.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
