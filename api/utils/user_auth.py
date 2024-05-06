import re, bcrypt

def validate_user(user_data: dict):
    name_regex = r'^[a-zA-ZÀ-ÿ]+(?: [a-zA-ZÀ-ÿ]+)*(?: [a-zA-ZÀ-ÿ]+)*$'
    registration_regex = r'^\d+$'

    name_is_valid = re.match(name_regex, user_data['name'])
    registration_is_valid = re.match(registration_regex, user_data['registration'])
    password_is_valid = user_data['password'] is not ""

    if name_is_valid and registration_is_valid and password_is_valid:
        return True
    return False


def hash_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=password, salt=salt)
    return hashed_password


def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)