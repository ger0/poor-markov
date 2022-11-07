#!/bin/python

import random
import click

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


def countLetters(words, msg=''):
    letter_count = 0
    letters = {}
    for i in words:
        letter_count += len(i)
        for letter in i:
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1

    # no whitespaces
    # print(msg + "Średnia liczba znaków na słowo:", letter_count / len(words))

    # whitespaces
    letter_count += len(words)
    for key in letters:
        letters[key] /= letter_count
    letters[' '] = len(words) / letter_count
    return letters


def get_results(degree, length):
    new_char = ' '
    result = "probability"
    prev = "".join(result[-degree:])
    if degree == 5:
        dict = fifth_dict
    elif degree == 3:
        dict = third_dict
    else:
        dict = first_dict

    # wygenerowany znak stopnia degree
    for _ in range(0, length - degree):
        if prev in dict:
            prob_char = list(dict[prev].keys())
            prob_val = list(dict[prev].values())
            [new_char] = random.choices(prob_char, prob_val)
            result += "".join(new_char)
            prev = (prev[-(degree - 1):] +
                    new_char) if degree != 1 else new_char
    # countLetters(result.split(' '), str(degree))
    return result


@click.command()
@click.argument('filename')
@click.option('--output', '-o', type=str, help="Output generated text to a file")
@click.option('--length', '-l', type=int, default=10000,
              show_default=True, help="Length of the generated text")
def main(filename, output, length):
    """Learn character probability from file specified by FILENAME
    and generate custom text"""
    in_file = open(filename, "r")
    out_file = open(output, "w") if output else None

    global_string = ""

    for line in in_file:
        global_string = line

    in_file.close()

    # get probabilities of next possible character based on 5 previous ones
    get_probabilities(global_string, 5, fifth_dict)

    deg = 5
    res = get_results(deg, length)
    res = res[deg:-1]
    if out_file:
        out_file.write(res)
        out_file.close()
    else:
        print(res)


main()
