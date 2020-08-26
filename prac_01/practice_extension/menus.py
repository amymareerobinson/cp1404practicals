"""
CP1404 2020 - Practice & Extension
Student Name: Amy Robinson
Program - Menus
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ").title()

print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid message")

    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
