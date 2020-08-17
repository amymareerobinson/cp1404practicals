"""
CP1404 2020 - Practical 3
Student Name: Amy Robinson
Program - Password Check
"""

MINIMUM_LENGTH = 6

password = input("Enter password: ")

while len(password) < MINIMUM_LENGTH:
    print("Invalid password length")
    password = input("Enter password: ")

password_length = len(password)

print("*" * password_length, end='')
