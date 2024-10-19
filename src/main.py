import bcrypt
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

def hash_password(password):
    """
    Uses bcrypt library to generate and return the hashed password
    """
    salt = bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(password.encode('utf-8'), salt)

def main():
    print('A valid password must:\n\t-Be at least 12 characters long')
    print('\t-Contain at least one lowercase letter (a-z)\n\t-Contain at least one uppercase letter (A-Z)')
    print('\t-Contain at least one number (0-9)\n\t-Contain at least one symbol (!-))\n')

    password = ''
    while (password != '0'):
        password = input('Enter a password (or enter 0 to terminate): ')
        if password == '0':
            return
        elif check_password(password):
            print(f'\nYour password {password} is valid!')
            print(f'Your encrypted password: {hash_password(password)}')
            return
        else:
            print(f'Invalid password.')

if __name__ == '__main__':
    main()