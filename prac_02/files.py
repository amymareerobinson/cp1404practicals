"""
CP1404 2020 - Practical 2
Student Name: Amy Robinson
Program - Files

Do-from-scratch Exercises
"""

# 1.
output_file = open("name.txt", "w")
output_name = input("Enter name: ")
print(output_name, file=output_file)
output_file.close()

# 2.
input_file = open("name.txt", "r")
input_name = input_file.read()
print("Your name is {}".format(input_name))
input_file.close()

# 3.
input_file = open("numbers.txt", "r")
file_contents_list = input_file.readlines()
sum_calculation = int(file_contents_list[0]) + int(file_contents_list[1])
print(sum_calculation)
input_file.close()

# 4.
input_file = open("numbers.txt", "r")
sum_of_numbers = 0

for line in input_file:
    number = int(line)
    sum_of_numbers += number

print(sum_of_numbers)
input_file.close()
