#!/bin/python

import random

MAX_VAL = 1000000
STR_LEN = 10000
'''
kolejnosc: [liczba wystapien, prawdopodobienstwo] - tuple
     a     b    c     d
a   0.1   0.2  0.3   0.1
b   0.2   0.1  0.2   0.1
c   0.1   0.1  0.4   0.2
d   0.0   0.2  0.1   0.3
'''

word_dict = {}
letters_after = {}


def init_dict():
    global word_dict
    global letters_after
    letters = list(range(ord('a'), ord('z') + 1))
    letters.append(ord(' '))
    letters.extend(list(range(ord('0'), ord('9') + 1)))

    for letter in letters:
        word_dict.setdefault(chr(letter), {})
        letters_after[letter] = 1
        for next in letters:
            word_dict[chr(letter)][chr(next)] = 0


def get_prob(words):
    global word_dict
    global letters_after
    it = iter(words)
    item = next(it)

    while True:
        next_item = next(it, '\0')
        if next_item == '\0':
            break

        # letters_after[item] += 1
        after = letters_after.setdefault(item, 1)
        after += 1 
        prob = word_dict[item][next_item]
        prob += 1
        word_dict[item][next_item] = prob

        item = next_item


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
    #print("Średnia liczba znaków na słowo:", letter_count / len(words))

    # ze spacjami
    letter_count += len(words)
    for key in letters:
        letters[key] /= letter_count
    letters[' '] = len(words) / letter_count
    '''
    for key in letters:
        print(key, letters[key])
    '''
    return letters


file = open("norm_wiki_sample.txt", "r")
global_words = []
global_string = ""

for line in file:
    global_words = line.split(' ')
    global_string = line

global_words = global_words[0:MAX_VAL]
global_string = global_string[0:MAX_VAL]

letters = countLetters(global_words)

init_dict()
get_prob(global_string)

generated = "probability"
# ostatni znak
prev = generated[-1] 
new_char = ' '

for i in range(0, STR_LEN):
    # wygenerowany znak 1 stopnia
    prob_char   = list(word_dict[prev].keys())
    prob_val    = list(word_dict[prev].values())
    [new_char]  = random.choices(prob_char, prob_val) 
    generated += "".join(new_char)
    prev = new_char
print(generated)

'''
generated = ""
for i in range(0, MAX_VAL):
    generated += "".join(random.choices(list(letters.keys()),
                                        list(letters.values())))
print(generated)
# countLetters(generated.split(' '))
'''
