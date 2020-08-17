"""
CP1404 2020 - Practical 2
Student Name: Amy Robinson
Program - Exception Handling

Answer the following questions:
1. When will a ValueError occur? When a non-numerical value is entered.
2. When will a ZeroDivisionError occur? When the denominator variable is 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, you could had an error checking loop instead.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Invalid denominator - Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:  # ValueError - if non-numerical value is entered
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:  # ZeroDivisionError - if zero value is entered
#     print("Cannot divide by zero!")
print("Finished.")
