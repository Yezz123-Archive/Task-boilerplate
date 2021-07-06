def validate_login(login):
    forbiddenchars = set('@')
    return login.strip() != '' and not any(
        (c in forbiddenchars) for c in login)


def validate_password(password):
    forbiddenchars = set()
    return password.strip() != '' and not any(
        (c in forbiddenchars) for c in password)


def validate_task_title(title):
    return title.strip() != ''