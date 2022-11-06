#!/bin/python

import random

MAX_VAL = 100000000
STR_LEN = 10000

# 1 rzad
first_dict = {}
# 3 rzad
third_dict = {}
# 5 rzad
fifth_dict = {}

def get_probabilities(words, degree, dict):
    global first_dict
    global third_dict
    global fifth_dict
    it = iter(words)
    items = []
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
global_string = ""

for line in file:
    global_string = line

global_string = global_string[0:MAX_VAL]

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
