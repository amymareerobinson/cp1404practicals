"""
CP1404 2020 - Practice and Extensions
Student Name: Amy Robinson
Program - Convert Temperatures
"""
INPUT_FILE = "temps_input.txt"
OUTPUT_FILE = "temps_output.txt"


def main():
    """read an INPUT_FILE of fahrenheit temperatures and print converted celsius temperatures to an OUTPUT_FILE"""

    input_file = open(INPUT_FILE, "r")
    output_file = open(OUTPUT_FILE, "w")

    for line in input_file:
        celsius = fahrenheit_to_celsius(float(line))
        print(f"{celsius:6.2f} C", file=output_file)

    input_file.close()
    output_file.close()


def fahrenheit_to_celsius(fahrenheit):
    """convert fahrenheit to celsius"""
    fahrenheit = 5 / 9 * (fahrenheit - 32)
    return fahrenheit


main()
