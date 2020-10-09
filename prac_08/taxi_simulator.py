"""
CP1404 2020 - Practical 8
Student Name: Amy Robinson
Program - Taxi Simulator
"""

from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Generate Taxi Simulator that uses Taxi and SilverServiceTaxi classes."""
    print("Let's drive")

    prius = Taxi("prius", 100)
    limo = SilverServiceTaxi("Limo", 100, 2)
    hummer = SilverServiceTaxi("Hummer", 200, 4)

    current_taxi = None
    taxis = [prius, limo, hummer]
    bill_to_date = 0

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            current_taxi = choose_taxi(bill_to_date, taxis)

        elif choice == "D":
            bill_to_date = drive_taxi(bill_to_date, current_taxi)

        else:
            print("Invalid input error message")

        print(MENU)
        choice = input(">>> ").upper()

    print(f"Total trip cost: {bill_to_date:.2f}")
    print(f"Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxi details."""
    for number, taxi in enumerate(taxis):
        print(f"{number} - {taxi}")


def get_taxi_number(taxis):
    """Get valid taxi number."""
    is_valid_input = False
    while not is_valid_input:
        try:
            taxi_number = int(input("Choose taxi: "))
            if taxi_number < 0:
                print("Invalid number")
            elif taxi_number not in range(len(taxis)):
                print("Invalid number")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    return taxi_number


def choose_taxi(bill_to_date, taxis):
    """Choose taxi."""
    print("Taxis available:")
    display_taxis(taxis)
    taxi_number = get_taxi_number(taxis)
    current_taxi = taxis[taxi_number]
    print(f"Bill to date: ${bill_to_date:.2f}")
    return current_taxi


def get_drive_distance():
    """Get valid drive distance."""
    is_drive_distance = False
    while not is_drive_distance:
        try:
            driven_distance = float(input("Drive how far? "))
            if driven_distance < 0:
                print("Invalid number")
            else:
                is_drive_distance = True
        except ValueError:
            print("Invalid (not an integer)")
    return driven_distance


def drive_taxi(bill_to_date, current_taxi):
    """Drive taxi."""
    current_taxi.start_fare()
    driven_distance = get_drive_distance()
    current_taxi.drive(driven_distance)
    print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
    bill_to_date += current_taxi.get_fare()
    print(f"Bill to date: ${bill_to_date:.2f}")
    return bill_to_date


main()
