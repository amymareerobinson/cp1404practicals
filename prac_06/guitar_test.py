"""
CP1404 2020 - Practical 4
Student Name: Amy Robinson
Program - Guitar Test
"""


class Guitar:
    """Represent a Guitar object"""
    CURRENT_YEAR = 2020
    VINTAGE_THRESHOLD = 50

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display Guitar details."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get the age of the Guitar."""
        return Guitar.CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if Guitar is vintage."""
        return Guitar.get_age(self) >= Guitar.VINTAGE_THRESHOLD


def run_tests():
    """Run tests to test the Guitar class."""
    print(Guitar.get_age(Guitar("Gibson L-5 CES", 1922)))
    print(Guitar.get_age(Guitar("Another Guitar", 2013)))

    print(Guitar.is_vintage)
    print(Guitar.is_vintage)


if __name__ == '__main__':
    run_tests()
