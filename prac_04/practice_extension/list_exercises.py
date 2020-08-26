"""
CP1404 2020 - Practice and Extensions
Student Name: Amy Robinson
Program - List Exercises
"""

# 1. Basic list operations
numbers = []

for i in range(5):
    number = int(input("Enter Number: "))
    while number < 0:
        print("Invalid number")
        number = int(input("Enter Number: "))
    numbers.append(number)

for number, line in enumerate(numbers, 1):
    print(f"Number {number}: {line}")

print(f"The first number is {numbers[0]}\n"
      f"The last number is {numbers[-1]}\n"
      f"The smallest number is {min(numbers)}\n"
      f"The largest number is {max(numbers)}\n"
      f"The average of the numbers is {sum(numbers)/len(numbers)}")

#  2. Indefinite set of strings

strings = []

string = input("Enter string: ")

while len(string) != 0:
    strings.append(string)
    string = input("Enter string: ")

list_length = len(strings)
repeated = []
for number in range(list_length):
    k = number + 1
    for j in range(k, list_length):
        if strings[number] == strings[j] and strings[number] not in repeated:
            repeated.append(strings[number])

if len(repeated) != 0:
    print(f"Strings repeated: {' '.join(repeated)}")
else:
    print("No repeated strings entered")
