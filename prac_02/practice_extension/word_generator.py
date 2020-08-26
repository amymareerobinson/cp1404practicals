"""
CP1404 - Practice & Extension
Author: Amy Robinson
Program - Word Generator

Random word generator - based on format of words
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

# word_format = input("Enter word format: ").lower()
# word = ""
#
# for kind in word_format:
#     if kind == "c":
#         word += random.choice(CONSONANTS)
#     else:
#         word += random.choice(VOWELS)

"""
Try and make the program more interesting For example:
a. Use wildcards for the vowels (#) and consonants (%) or either (*)
and make alphabetical characters use that actual character
- e.g. the format "%re#l" might produce a word like "greatly" or "breuzla"

b. Automatically (randomly) generate the word_format variable.
"""

length = 4
punctuation = '%#'
word = ""
word_format = ""

for i in range(length):
    word_format += random.choice(string.ascii_lowercase) + random.choice(punctuation)

for kind in word_format:
    if kind == "#":
        word += random.choice(VOWELS)
    elif kind == "%":
        word += random.choice(CONSONANTS)
    elif kind != "#" or kind != "%":
        word += kind

print(word)
