"""
CP1404 2020 - Practical 2
Student Name: Amy Robinson
Program - Randoms
"""

# imports 'random' module
import random

print(random.randint(5, 20))  # generates a random integer between 5 and 20
print(random.randrange(3, 10, 2))  # generates a random odd integer between 3 and 10
print(random.uniform(2.5, 5.5))  # generates a random decimal between 2.5 and 5.5

"""
What did you see on line 1? 14
What was the smallest number you could have seen, what was the largest?
smallest number = 5
largest number = 20

What did you see on line 2? 7
What was the smallest number you could have seen, what was the largest?
smallest = 3
largest = 10
Could line 2 have produced a 4? No

What did you see on line 3? 4.136196483497342
What was the smallest number you could have seen, what was the largest?
smallest = 2.5
largest = 10
"""

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
