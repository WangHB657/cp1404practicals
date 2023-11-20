MIN_PASSWORD_LENGTH = 8  # Minimum password length
valid_password = False

while not password:
    password = input("Enter a password: ")
    if len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password should be at least {MIN_PASSWORD_LENGTH} characters long. Try again.")
    else:
        password = True

print("*" * len(password))
