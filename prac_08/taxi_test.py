"""
CP1404 2020 - Practical 8
Student Name: Amy Robinson
Program - Taxi Test
"""

from prac_08.taxi import Taxi

# 1. Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km
new_taxi = Taxi("Prius 1", 100)

# 2. Drive the taxi 40km
new_taxi.drive(40)

# 3. Print the taxi's details and the current fare
new_taxi.get_fare()
print(f"Taxi's details: {new_taxi}\n  "
      f"Current fare: {new_taxi.get_fare()}")

# 4. Restart the meter (start a new fare) and then drive the car 100km
new_taxi.start_fare()
new_taxi.drive(100)

# 5. Print the details and the current fare
print(f"Taxi's details: {new_taxi}\n  "
      f"Current fare: {new_taxi.get_fare()}")
