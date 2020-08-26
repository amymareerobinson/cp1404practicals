"""
CP1404 2020 - Practice and Extensions
Student Name: Amy Robinson
Program - Total Income

Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        incomes.append(income)

    display_income_report(incomes)


def display_income_report(incomes):
    print("\nIncome Report\n-------------")
    total = 0
    for number, month in enumerate(incomes, 1):
        total += month
        print(f"Month {number:2} - Income: ${month:10.2f} Total: ${total:10.2f}")


main()
