"""
CP1404 2020 - Practical 3
Student Name: Amy Robinson
Program - Password Check
"""

MINIMUM_LENGTH = 6


def main():
    """check for valid password and display length in stars"""

    password = get_password()

    number_of_stars = count_characters(password)

    print(number_of_stars * "*", end="")


def get_password():
    """get a valid password"""
    password = input("Enter password: ")

    while len(password) < MINIMUM_LENGTH:
        print("Invalid password length")
        password = input("Enter password: ")
    return password


def count_characters(string_variable):
    """count the number of characters in a string_variable"""
    count_character = len(string_variable)
    return count_character


main()
