"""
CP1404 2020 - Practical 4
Student Name: Amy Robinson
Program - Quick Picks
"""

import random

NUMBERS_IN_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))

for i in range(number_of_quick_picks):
    quick_pick_numbers = []
    for j in range(NUMBERS_IN_LINE):
        random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while random_number in quick_pick_numbers:
            random_number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        quick_pick_numbers.append(random_number)
    quick_pick_numbers.sort()

    print(" ".join(f"{random_number:2}" for random_number in quick_pick_numbers))
