email_dict = {}
email = input("Email: ")

while email != "":
    name_part = email.split('@')[0]
    name_parts = name_part.split('.')
    extracted_name = ' '.join(part.title() for part in name_parts)

    confirmation = input(f"Is your name {extracted_name}? (Y/n) ").strip().lower()
    if confirmation in ['', 'y', 'yes']:
        name = extracted_name
    else:
        name = input("Name: ").strip().title()

    email_dict[email] = name
    email = input("Email: ")

for email, name in email_dict.items():
    print(f"{name} ({email})")

