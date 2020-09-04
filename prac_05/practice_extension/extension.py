"""
CP1404 2020 - Practice & Extension
Student Name: Amy Robinson
Program - Extension
"""
# Program 1.
CURRENT_YEAR = 2020
birthday_dict = {}
ages = []
for i in range(1):
    name = input("Name: ")
    date_of_birth = input("Date of Birth (DD/MM/YYYY): ")
    birthday_dict[name] = date_of_birth


for name, date_of_birth in birthday_dict.items():
    dob = birthday_dict[name].split("/")
    age = CURRENT_YEAR - int(dob[-1])
    print(f"Name: {name} Age: {age}")

print(birthday_dict)


# Program 2.
def main():
    """Convert parallel lists into a dictionary."""
    names = ["Jack", "Jill", "Harry"]
    dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]

    print(generate_a_dictionary(names, dates_of_birth))


def generate_a_dictionary(list_1, list_2):
    """Generate a dictionary from two lists."""
    dictionary = {}
    for key in list_1:
        for value in list_2:
            dictionary[key] = value
    return dictionary


main()

# Program 3.
# Extend your name & address program
# with file loading and saving (and any other fun things you'd like to add).
