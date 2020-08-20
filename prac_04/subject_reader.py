"""
CP1404 2020 - Practical 4
Student Name: Amy Robinson
Program - Subject Reader
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        subjects.append(parts)
    input_file.close()
    return subjects


def display_subject_details(subjects):
    """display subject details from subjects list"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:3} students")


main()
