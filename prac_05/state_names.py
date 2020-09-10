"""
CP1404 2020 - Practical 5
Student Name: Amy Robinson
Program - State Names

State names in a dictionary
File needs reformatting
"""

# Reformat this file so the dictionary code follows PEP 8 convention
LONGEST_STATE_CODE = 3

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales",
                "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory",
                "VIC": "Victoria", "TAS": "Tasmania"}

print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()

while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()


# ON PAPER FIRST:
# LONGEST_STATE_CODE = 3
# for state_code, state in CODE_TO_NAME.items():
#     print(f"{state_code:LONGEST_STATE_CODE} is {state}")

for state_code, state in CODE_TO_NAME.items():
    print(f"{state_code:LONGEST_STATE_CODE} is {state}")
