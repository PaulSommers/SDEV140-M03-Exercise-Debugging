"""
Author: Paul Sommers
Date written: 11/4/2024
Assignment: Module 03 Peer Exercise - Debugging
Short Desc: This program calculates the Flesch Index and the Grade Level Equivalent of a text file.
            It has been modified to fix a bug.
"""

# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    last_lettervowel = False  # Boolean to track consecutive vowels
    for char in word:
        if char in vowels:
            if not last_lettervowel:  # Only count if it's not a consecutive vowel
                syllables += 1
            last_lettervowel = True  # Set True
        else:
            last_lettervowel = False  # Reset if the current letter is not a vowel
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")