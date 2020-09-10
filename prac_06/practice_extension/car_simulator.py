"""
CP1404 2020 - Practice & Extension
Student Name: Amy Robinson
Program - Car Simulator
"""
from prac_06.car import Car

MENU = "Menu:\n" \
       "d) drive\n" \
       "r) refuel\n" \
       "q) quit"

STARTING_FUEL = 100


def main():
    """Stimulate a car."""
    print("Let's drive!")
    car_name = input("Enter your car name: ")

    car_details = Car(name=car_name, fuel=STARTING_FUEL)

    display_car_details(car_details, car_name)
    print(MENU)
    menu_choice = input("Enter your choice: ").upper()

    while menu_choice != 'Q':
        if menu_choice == 'D':
            stimulate_drive(car_details)

        elif menu_choice == 'R':
            refuel_car(car_details)

        else:
            print("Invalid choice")

        print()
        display_car_details(car_details, car_name)
        print(MENU)
        menu_choice = input("Enter your choice: ").upper()

    print(f"Good bye {car_name}'s driver.")


def display_car_details(car_details, car_name):
    print(f"{car_name}, fuel={car_details.fuel}, odo={car_details.odometer}")


def get_valid_integer(variable_name, prompt):
    """Get valid integer."""
    is_valid_integer = False
    while not is_valid_integer:
        try:
            integer = int(input(prompt))
            if integer < 0:
                print(f"{variable_name} must be >= 0")
            else:
                is_valid_integer = True
        except ValueError:
            print("Invalid. Must be an integer.")
    return integer


def stimulate_drive(car_details):
    """stimulate a drive"""
    distance = get_valid_integer("distance", "How many km do you wish to drive? ")

    if distance > car_details.fuel:
        print(f"The car drove {car_details.fuel}km and ran out of fuel.")
    else:
        print(f"The car drove {distance}km.")
    car_details.drive(distance)


def refuel_car(car_details):
    """Refuel car."""
    fuel = get_valid_integer("fuel", "How many units of fuel do you want to add to the car? ")
    car_details.add_fuel(fuel)


main()
