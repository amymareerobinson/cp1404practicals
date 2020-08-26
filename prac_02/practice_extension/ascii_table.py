"""
CP1404 - Practice & Extension
Student Name: Amy Robinson
Program - ASCII Table
"""

LOWER_NUMBER = 33
UPPER_NUMBER = 127

# character = input("Enter a character: ")
# number_of_character_value = ord(character)
# print(f"The ASCII code for {character} is {number_of_character_value}")
#
# number = int(input(f"Enter a number between {LOWER_NUMBER} and {UPPER_NUMBER}: "))
#
# while number < LOWER_NUMBER or number > UPPER_NUMBER:
#     print("Invalid number!")
#     number = int(input(f"Enter a number between {LOWER_NUMBER} and {UPPER_NUMBER}: "))
#
# character_of_number_value = chr(number)
# print(f"The character for {number} is {character_of_number_value}")
#
# for number in range(LOWER_NUMBER, UPPER_NUMBER):
#     character_of_number_value = chr(number)
#     print(f"{number:>3}  {character_of_number_value}")
#


# ASCII Columns Challenge
number_of_columns = int(input("Enter number of columns: "))
number_of_values = UPPER_NUMBER - LOWER_NUMBER + 1
number_of_rows = number_of_values // number_of_columns

for row in range(number_of_rows + 1):
    first_row_number = LOWER_NUMBER + row

    for column in range(number_of_columns - 1):
        number_value = first_row_number + (column * number_of_rows)
        character_value_number = chr(number_value)
        print(f"{number_value:5}  {character_value_number}", end="")
        first_row_number += 1

    column = 0
    number_value = first_row_number + ((column + 1) * number_of_rows)

    if number_value <= UPPER_NUMBER:
        character_value_number = chr(number_value)
        print(f"{number_value:5}  {character_value_number}", end="")
    print()
