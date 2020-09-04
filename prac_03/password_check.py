"""
CP1404 2020 - Practical 3
Student Name: Amy Robinson
Program - Password Check
"""

MINIMUM_LENGTH = 6


def main():
    """check for valid password and display length in stars"""

    password = get_password()

    display_length_in_star_characters(password)


def get_password():
    """Get a valid password."""
    password = input("Enter password: ")

    while len(password) < MINIMUM_LENGTH:
        print("Invalid password length")
        password = input("Enter password: ")
    return password


def display_length_in_star_characters(string_variable):
    """Display the length of the string_variable in star characters."""
    count_character = len(string_variable)
    print(count_character * "*", end="")


main()
