"""
CP1404 2020 - Practical 4
Student Name: Amy Robinson
Program - Guitar
"""

from prac_06.guitar_test import Guitar


def main():
    """Get Guitar details to display, formatting: name, year, cost and whether it's vintage."""
    print("My guitars!")
    guitars = []
    # guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost} added.")
        name = input("Name: ")

    print("... snip ...")

    print("These are my guitars:")

    for number, guitar in enumerate(guitars, 1):
        is_vintage = Guitar.is_vintage
        vintage_string = "(vintage)" if is_vintage is True else ''
        print(f"Guitar {number}: {guitar.name:.20} ({guitar.year}), ${guitar.cost:10,.2f} {vintage_string}")


main()
