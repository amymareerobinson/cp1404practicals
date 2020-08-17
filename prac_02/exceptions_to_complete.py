"""
CP1404 2020 - Practical 2
Student Name: Amy Robinson
Program - Exceptions to Complete

Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        # TODO: this line
        result = int(input("Enter result: "))
        # TODO: this line
        finished = True

    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")

print("Valid result is:", result)
