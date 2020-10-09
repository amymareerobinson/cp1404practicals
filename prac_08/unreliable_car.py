"""
CP1404 2020 - Practical 8
Student Name: Amy Robinson
Program - Unreliable Car
"""

from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Represents an UnreliableCar object."""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car if random generated number is less than the Car's reliability."""
        if randint(0, 100) < self.reliability:
            driven_distance = super().drive(distance)
        else:
            driven_distance = 0
        return driven_distance
