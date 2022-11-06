#!/bin/python

import random
from itertools import permutations

MAX_VAL = 100000000
STR_LEN = 10000

# 1 rzad
first_dict = {}

# 3 rzad
third_dict = {}

# 5 rzad
fifth_dict = {}


def init_dicts():
    global first_dict
    global third_dict
    global fifth_dict

    letters = list(range(ord('a'), ord('z') + 1))
    letters.append(ord(' '))
    letters.extend(list(range(ord('0'), ord('9') + 1)))

    for letter in letters:
        first_dict.setdefault(chr(letter), {})

        for n1 in letters:
            first_dict[chr(letter)][chr(n1)] = 0
            for n2 in letters:
                for n3 in letters:
                    chars = "".join([chr(n1) + chr(n2) + chr(n3)])
                    third_dict.setdefault(chars, {})[chr(letter)] = 0


def get_first_probabilities(words):
    global first_dict

    it = iter(words)
    item = next(it)

    while True:
        next_item = next(it, '\0')
        if next_item == '\0':
            break

        prob = first_dict[item][next_item]
        prob += 1
        first_dict[item][next_item] = prob

        item = next_item


def get_probabilities(words, degree, dict):
    global first_dict
    global third_dict
    global fifth_dict
    it = iter(words)
    items = []
    #items = [next(it), next(it), next(it)]
    for _ in range(degree):
        items.append(next(it))

    while True:
        next_item = next(it, '\0')
        if next_item == '\0':
            break

        chars = "".join(items)

        if chars in dict:
            if next_item in dict[chars]:
                dict[chars][next_item] += 1
            else:
                dict.setdefault(chars, {})[next_item] = 1

        else:
            dict.setdefault(chars, {})[next_item] = 1

        items = items[1:] 
        items.append(next_item)


def countLetters(words, msg = ''):
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
    print(msg + "Średnia liczba znaków na słowo:", letter_count / len(words))

    # ze spacjami
    letter_count += len(words)
    for key in letters:
        letters[key] /= letter_count
    letters[' '] = len(words) / letter_count
    return letters

def get_results(degree):
    new_char = ' '
    result = "probability"
    prev = "".join(result[-degree:])
    if degree == 3:
        dict = third_dict
    elif degree == 5:
        dict = fifth_dict
    else:
        dict = first_dict

    # wygenerowany znak stopnia
    for _ in range(0, STR_LEN):
        if prev in dict:
            prob_char   = list(dict[prev].keys())
            prob_val    = list(dict[prev].values())
            [new_char]  = random.choices(prob_char, prob_val) 
            result += "".join(new_char)
            prev = (prev[-(degree - 1):] + new_char) if degree != 1 else new_char
    countLetters(result.split(' '), str(degree))
    return result


file = open("norm_wiki_sample.txt", "r")
#global_words = []
global_string = ""

for line in file:
    #global_words = line.split(' ')
    global_string = line

#global_words = global_words[0:MAX_VAL]
global_string = global_string[0:MAX_VAL]

#letters = countLetters(global_words)

init_dicts()
get_probabilities(global_string, 1, first_dict)
get_probabilities(global_string, 3, third_dict)
get_probabilities(global_string, 5, fifth_dict)

# Średnia liczba znaków na słowo (przybliżenie 1 rzędu): 4.9916217833632555
# Średnia liczba znaków na słowo (przybliżenie 3 rzędu): 4.906784660766962
# Średnia liczba znaków na słowo: 4.945368171021378

for deg in [1, 3, 5]:
    res = get_results(deg)
    
    if deg == 5:
        print(res)
