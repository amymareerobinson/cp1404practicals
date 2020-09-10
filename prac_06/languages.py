"""
CP1404 2020 - Practical 4
Student Name: Amy Robinson
Program - Languages
"""

from prac_06.programming_language import ProgrammingLanguage

"""
ON PAPER FIRST:
dynamic_languages = []
    print(f"The dynamically typed languages are:")

    for dynamic_language in programming_languages:
        if dynamic_language.is_dynamic() is True:
            dynamic_languages.append(dynamic_language)

    for language in dynamic_languages:
        print(language)
"""


def main():
    """Display the dynamically typed programming languages."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(f"{ruby}\n{python}\n{visual_basic}")
    print("-" * 70)

    programming_languages = [ruby, python, visual_basic]

    dynamic_languages = []
    print(f"The dynamically typed languages are:")

    for dynamic_language in programming_languages:
        if dynamic_language.is_dynamic() is True:
            dynamic_languages.append(dynamic_language)

    for language in dynamic_languages:
        print(language)


main()
