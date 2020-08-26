"""
CP1404 2020 - Practice and Extensions
Student Name: Amy Robinson
Program - Score Results
"""

import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
OUTPUT_FILE = "results.txt"


def main():
    """generate score results for a number of scores and print to OUTPUT_FILE"""
    number_of_scores = int(input("Enter number of scores: "))

    out_file = open(OUTPUT_FILE, 'w')  # opens 'OUTPUT_FILE' for writing

    for number in range(number_of_scores):
        score = display_random_score(MINIMUM_SCORE, MAXIMUM_SCORE)
        score_result = return_score_result(score)

        print(f"{score:2} is {score_result}", file=out_file)

    out_file.close()  # closes out_file variable


def return_score_result(score):
    """generate a score result for parameter score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def display_random_score(minimum_score, maximum_score):
    """display a random score between minimum_score and maximum_score"""
    random_score = random.randint(minimum_score, maximum_score)
    return random_score


main()
