from werkzeug.security import check_password_hash, generate_password_hash


def check_user_password(user, password):
    return check_password_hash(user.password, password)


def hashify_password(password):
    return generate_password_hash(password, salt_length=64)