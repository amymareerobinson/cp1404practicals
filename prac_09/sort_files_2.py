"""
CP1404 2020 - Practical 9
Student Name: Amy Robinson
Program - Sort Files 2
"""

import os
import shutil

DIRECTORY = 'FilesToSort'


def main():
    """Create a subdirectory with each new category the user inputs."""
    extension_dict = {}
    os.chdir(DIRECTORY)

    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename[filename.find('.') + 1:]
        if extension not in extension_dict:
            category = input(f"What category would you like to sort {extension} extensions into? ")
            extension_dict[extension] = category
        try:
            os.mkdir(category)
        except FileExistsError:
            pass

        shutil.move(filename, extension_dict[extension])


main()
