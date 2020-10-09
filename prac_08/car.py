"""
CP1404 2020 - Practical 8
Student Name: Amy Robinson
Program - Car
"""


class Car:
    """Represent a Car object."""

    # 7. Now add a name field to the Car class (in car.py),
    # and adjust the __init__ and __str__ methods to set and display this respectively.
    def __init__(self, name='', fuel=0):
        """Initialise a Car instance.

        fuel: float, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance

    # 6. Now add the __str__ method to the Car class in car.py.
    def __str__(self):
        """Display Car details."""
        return f"Car={self.name}, fuel={self.fuel}, odometer={self.odometer}"
