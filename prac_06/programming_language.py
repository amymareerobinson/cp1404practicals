"""
CP1404 2020 - Practical 4
Student Name: Amy Robinson
Program - Programming Language
"""


class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, field, typing, reflection, year):
        """Initialise a Programming Language instance."""
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if the Programming Language is dynamic."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Display Programming Language details."""
        return f"{self.field}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
