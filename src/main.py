def check_password(password):
    """
    Takes a string and returns true if it is a valid password.
    Otherwise, returns false.

    A valid password is at least 12 characters long, and has at least one
    of each of the following: lowercase letter (a-z), uppercase letter (A-Z),
    number (0-9), symbol (!-))
    """

    if type(password) != str:
        raise TypeError('Non-string passed to check_password')

    if len(password) < 12:
        return False

    symbol_set = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')'}
    has_type = set()
    for char in password:
        if 'a' <= char <= 'z':
            has_type.add('lowercase')
        elif 'A' <= char <= 'Z':
            has_type.add('uppercase')
        elif '0' <= char <= '9':
            has_type.add('number')
        elif char in symbol_set:
            has_type.add('symbol')
        else:
            return False

    if has_type == {'lowercase', 'uppercase', 'number', 'symbol'}:
        return True
    else:
        return False

