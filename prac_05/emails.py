"""
CP1404 2020 - Practical 5
Student Name: Amy Robinson
Program - Emails
"""


def main():
    """Generate a dictionary of names and emails"""
    email_dict = {}

    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        verify_name = input(f"Is your name {name}? (Y/n) ").lower()

        if verify_name == 'y' or verify_name == "":
            email_dict[email] = name

        elif verify_name == 'n' or verify_name == 'no':
            name = input("Name: ").title()
            email_dict[email] = name

        else:
            print("Invalid verification, name could not be entered!")

        email = input("Email: ")

    for email, name in email_dict.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract name from email."""
    email = email.split("@")
    name = ' '.join(email[0].split(".")).title()
    return name


main()
