"""
CP1404 2020 - Practice & Extension
Student Name: Amy Robinson
Program - Sequences
"""

MENU = "Enter (E)ven, (O)dd, (S)quares to show sequence or (Q)uit"

x = int(input("Enter x number: "))
y = int(input("Enter y number: "))

print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "E":
        for i in range(x, y + 1):
            if i % 2 == 0:
                print(i, end=' ')
    elif choice == "O":
        for i in range(x, y + 1):
            if i % 2 != 0:
                print(i, end=' ')
    elif choice == "S":
        for i in range(x, y + 1):
            print(i * i, end=' ')

    else:
        print("Invalid message")

    print()
    print(MENU)
    choice = input(">>> ").upper()

print("Finished.")
