"""
CP1404 2020 - Practical 4
Student Name: Amy Robinson
Program - Lists Warmup
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]            = 3
# numbers[-1]           = 2
# numbers[3]            = 1
# numbers[:-1]          = [3, 1, 4, 1, 5, 9]
# numbers[3:4]          = [1]
# 5 in numbers          = True
# 7 in numbers          = False
# "3" in numbers        = False
# numbers + [6, 5, 3]   = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

# Write Python expressions (in the same Python file) to achieve the following:
# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = '10'
print(numbers)

# 2. Change the last element of numbers to 1
numbers[-1] = 1
print(numbers)

# 3. Get all the elements from numbers except the first two (slice)
numbers = numbers[2:]
print(numbers)

# 4. Check if 9 is an element of numbers
numbers = 9 in numbers
print(numbers)