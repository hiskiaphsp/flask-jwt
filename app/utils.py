from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    """
    Hash a plain text password.
    :param password: Plain text password
    :return: Hashed password
    """
    return generate_password_hash(password)

def verify_password(hashed_password, password):
    """
    Verify a plain text password against the hashed version.
    :param hashed_password: Hashed password from the database
    :param password: Plain text password
    :return: Boolean indicating if passwords match
    """
    return check_password_hash(hashed_password, password)
