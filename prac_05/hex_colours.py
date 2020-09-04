"""
CP1404 2020 - Practical 5
Student Name: Amy Robinson
Program - Hex Colours
"""

HEX_COLOURS = {"blueviolet": "#8a2be2", "coral": "#ff7f50",
               "firebrick": "#b22222", "forestgreen": "#228b22",
               "hotpink": "#ff69b4", "brown": "#a52a2a",
               "chocolate": "#d2691e", "floralwhite": "#fffaf0",
               "navyblue": "#000080", "light": "#eedd82"}
print(HEX_COLOURS)

colour = input("Enter a hex colour: ").lower()

while colour != "":
    if colour in HEX_COLOURS:
        print(f"{colour} code is {HEX_COLOURS[colour]}")
    else:
        print("Invalid colour name")

    colour = input("Enter a hex colour: ").lower()
