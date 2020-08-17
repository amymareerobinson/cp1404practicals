"""
CP1404 2020 - Practical 1
Student Name: Amy Robinson
Program - Shop Calculator
"""

DISCOUNT = .10  # As a decimal (e.g. 0.10 is 10%)
total_price = 0

number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price = float(input("Price of item: "))
    # calculates a running addition for total_price and price
    total_price += price

if total_price > 100:
    total_price = total_price - (total_price * DISCOUNT)

print(f"Total price for {number_of_items} items is ${total_price:.2f}")
