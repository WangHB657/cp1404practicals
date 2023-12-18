"""
function get_password()
    valid_password = False
    while not valid_password
        get password
        if length of password < MIN_PASSWORD_LENGTH
            print "Password should be at least 8 characters long. Try again."
        else
            valid_password = True
    return password

function print_password_asterisks(password)
    print "*" * len(password

function main()
    password = get_password()
    print_password_asterisks(password)
"""


MIN_PASSWORD_LENGTH = 8  # Minimum password length


def get_password():
    valid_password = False
    while not valid_password:
        password = input("Enter a password: ")
        if len(password) < MIN_PASSWORD_LENGTH:
            print(f"Password should be at least {MIN_PASSWORD_LENGTH} characters long. Try again.")
        else:
            valid_password = True
    return password


def print_password_asterisks(password):
    print("*" * len(password))


def main():
    password = get_password()
    print_password_asterisks(password)


main()
