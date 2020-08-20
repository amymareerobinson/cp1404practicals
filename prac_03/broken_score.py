"""
CP1404 2020 - Practical 3
Student Name: Amy Robinson
Program - Broken Score
"""

import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100


def main():
    """generate scores and print the results"""

    # Takes in a user score and prints the result
    score = int(input("Enter score: "))
    score_result = display_score_result(score)
    print(f"{score:2} is {score_result}")

    # Generates a random score and prints the result
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    random_score_result = display_score_result(random_score)
    print(f"{random_score:2} is {random_score_result}")


def display_score_result(score):
    """display a score result from variable score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
