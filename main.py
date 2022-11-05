#!/bin/python

import random

MAX_VAL = 10000


def countLetters(words):
    letter_count = 0
    letters = {}
    for i in words:
        letter_count += len(i)
        for letter in i:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1

    # bez spacji
    print("Średnia liczba znaków na słowo:", letter_count / len(words))

    # ze spacjami
    letter_count += len(words)
    for key in letters:
        letters[key] /= letter_count
    letters[' '] = len(words) / letter_count
    for key in letters:
        print(key, letters[key])
    return letters


file = open("norm_wiki_sample.txt", "r")
global_words = []

for line in file:
    global_words = line.split(' ')

global_words = global_words[0:MAX_VAL]
letters = countLetters(global_words)

generated = ""
for i in range(0, MAX_VAL):
    generated += "".join(random.choices(list(letters.keys()),
                                        list(letters.values())))
print(generated)
# countLetters(generated.split(' '))
