"""
CP1404 - Practice and Extensions
Author: Amy Robinson
Program - Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""

import random
import string

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

"""
Get the word format from the user so they can customise it.
Convert it to lowercase using a str method.
"""

word_format = input("Enter word format: ").lower()
word = ""

for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)
