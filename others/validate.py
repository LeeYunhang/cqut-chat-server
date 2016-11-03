import re


def validate_mob_number(mob_number):
    return re.match('^[0-9]{11}$', mob_number)


def validate_username(username):
    if username is None:
        return
    elif len(username) < 4 or len(username) > 16:
        return
    elif re.match(pattern='[\'\" ]', string=username):
        return

    return True


def validate_password(password):
    if password is None:
        return
    elif len(password) < 6 or len(password) > 16:
        return
    elif re.match(pattern='[\'\"]', string=password):
        return

    return True