"""
CP1404 2020 - Practical 8
Student Name: Amy Robinson
Program - Silver Service Taxi
"""

from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes flagfall and fanciness charges"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent classes Taxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the fare like parent plus flagfall charge."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return the string like Taxi but with flagfall charge."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
