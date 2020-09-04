"""
CP1404 2020 - Practice & Extension
Student Name: Amy Robinson
Program - Practice
"""

# Program 1 - Friends' Names and Addresses
MENU = "Menu:\n" \
       "E - Enter a new name and address\n" \
       "C - Change an address for an existing entry\n" \
       "P - Print the address for a name you choose\n" \
       "Q - Quit"

FILENAME = "address_data.txt"
NAME_INDEX = 0
ADDRESS_INDEX = 1


def main():
    """Generate an address file that's imported, updated and stored in FILENAME."""
    name_address_dict = load_data_to_dictionary()
    print(MENU)
    choice = input(">>> ").upper()

    while choice != 'Q':
        print(name_address_dict)

        if choice == 'E':
            name = get_valid_name("Name: ")
            address = get_address("Address: ")
            name_address_dict[name] = address

        elif choice == 'C':
            name = get_valid_name("Name for new address: ").lower()
            while name not in name_address_dict:
                print("Invalid; name not in dictionary")
                name = input("Name for new address: ").lower()

            new_address = get_address("New address: ")
            name_address_dict[name] = new_address

        elif choice == 'P':
            name = get_valid_name("Name to retrieve address: ").lower()
            while name not in name_address_dict:
                print("Invalid; name not in dictionary")
                name = input("Name to retrieve address: ").lower()

            print(f"{name}'s address is {name_address_dict[name]}")

        else:
            print("Invalid choice")

        print(MENU)
        choice = input(">>> ").upper()

    overwrite_data_to_file(name_address_dict)


def load_data_to_dictionary():
    """load data to a dictionary."""
    input_file = open(FILENAME, "r")
    dictionary = {}

    for line in input_file:
        line = line.strip().split(',')
        dictionary[line[NAME_INDEX]] = line[ADDRESS_INDEX]

    input_file.close()
    return dictionary


def get_address(prompt):
    """Get address."""
    new_address = input(prompt).lower()
    return new_address


def get_valid_name(prompt):
    """Get valid name."""
    name = input(prompt).lower()
    return name


def overwrite_data_to_file(name_address_dict):
    """Overwrite data to file."""
    output_file = open(FILENAME, "w")
    for name, address in name_address_dict.items():
        print(f"{name}, {address}", file=output_file)

    output_file.close()


main()


# Program 2 - Electricity Bill
print("Electricity bill estimator 2.0")

tariff_dict = {"11": 0.244618, "31": 0.136928}

tariff = input("Which tariff? 11 or 31: ")

daily_use_kWh = float(input("Enter daily use in kWh: "))
number_billing_days = int(input("Enter number of billing days: "))

estimated_bill = tariff_dict[tariff] * daily_use_kWh * number_billing_days

print(f"Estimated bill: ${estimated_bill:.2f}")