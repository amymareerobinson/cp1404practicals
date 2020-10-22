"""
CP1404 2020 - Practical 10
Student Name: Amy Robinson
Program - Wiki
"""
import wikipedia

phrase = input("Enter page title/ or search phrase: ")

while phrase != '':
    try:
        page = wikipedia.page(phrase)
        print(f"Page title: {page.title}\n"
              f"Page Summary: {page.summary}\n"
              f"Page URL: {page.url}")

    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)

    phrase = input("Enter page title/ or search phrase: ")
