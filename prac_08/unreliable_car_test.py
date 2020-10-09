"""
CP1404 2020 - Practical 8
Student Name: Amy Robinson
Program - Unreliable Car Test
"""

from prac_08.unreliable_car import UnreliableCar

# create a new unreliable car with name "Bubblebee", 100 units of fuel, reliability of 0% and 100%
unreliable_unreliable_car = UnreliableCar("Bubblebee", 100, 0)
reliable_unreliable_car = UnreliableCar("Bubblebee", 100, 100)

# Drive the unreliable car 40 km
unreliable_unreliable_car.drive(40)
print(f"Unreliable car at {unreliable_unreliable_car.reliability}%: {unreliable_unreliable_car}")
reliable_unreliable_car.drive(40)
print(f"Reliable car at {reliable_unreliable_car.reliability}%: {reliable_unreliable_car}")
