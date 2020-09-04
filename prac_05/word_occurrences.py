"""
CP1404 2020 - Practical 5
Student Name: Amy Robinson
Program - Word Occurrences
"""

word_count_dict = {}

text = input("Text: ")
words = sorted(text.split())

for word in words:
    word_count_dict[word] = word_count_dict.get(word, 0) + 1

longest_word = max((len(word) for word in words))

for text, count in word_count_dict.items():
    print(f"{text:{longest_word}} : {count}")
