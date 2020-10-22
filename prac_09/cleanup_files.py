"""
CP1404 2020 - Practical 9
Student Name: Amy Robinson
Program - Cleanup Files
"""

import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')

    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        for filename in filenames:
            new_name = get_fixed_filename(filename)
            print(f"Renaming {filename} to {new_name}")

            original_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(original_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    empty_string = ' '
    filename.replace(" ", "_").replace(".TXT", ".txt")
    if "_" not in filename:
        new_name = "_".join(''.join(empty_string + char if char.isupper()
                                    else char for char in filename).strip(empty_string).split(empty_string))

    else:
        new_name = "_".join(filename.split("_")).title()

    return new_name


main()
