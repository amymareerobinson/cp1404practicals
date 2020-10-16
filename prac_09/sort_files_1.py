"""
CP1404 2020 - Practical 9
Student Name: Amy Robinson
Program - Sort Files 1
"""

import os
import shutil

DIRECTORY = 'FilesToSort'


def main():
    """Create a subdirectory with each new extension the program finds."""
    os.chdir(DIRECTORY)

    filenames = [name for name in os.listdir('.')]
    for filename in filenames:
        file = filename[filename.find('.')+1:]
        directory = str(file)
        try:
            os.mkdir(directory)
        except FileExistsError:
            pass

        shutil.move(filename, directory)


main()
