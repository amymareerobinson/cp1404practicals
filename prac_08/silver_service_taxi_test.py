"""
CP1404 2020 - Practical 8
Student Name: Amy Robinson
Program - Silver Service Taxi Test
"""

from prac_08.silver_service_taxi import SilverServiceTaxi

# Create new silver service taxi with name "Silver Fox", 100,
new_silver_service_taxi = SilverServiceTaxi("Silver Fox", 100, 2)

# Start new fare
new_silver_service_taxi.start_fare()

# Drive 18 km
new_silver_service_taxi.drive(18)

# Print SilverServiceTaxi details and current fare
print(f"Silver Service Taxi's details: {new_silver_service_taxi},\n"
      f"                 Current fare:  {new_silver_service_taxi.get_fare()}")

# Drive another 18 km
new_silver_service_taxi.drive(18)

# Print SilverServiceTaxi details and current fare
print(f"Silver Service Taxi's details: {new_silver_service_taxi},\n"
      f"                 Current fare:  {new_silver_service_taxi.get_fare()}")
