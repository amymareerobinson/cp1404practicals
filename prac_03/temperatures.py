"""
CP1404 2020 - Practical 3
Student Name: Amy Robinson
Program - Temperatures
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """generate a temperature conversion menu between celsius and fahrenheit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def celsius_to_fahrenheit(celsius):
    """convert celsius to fahrenheit"""
    celsius = celsius * 9.0 / 5 + 32
    return celsius


def fahrenheit_to_celsius(fahrenheit):
    """convert fahrenheit to celsius"""
    fahrenheit = 5 / 9 * (fahrenheit - 32)
    return fahrenheit


main()
