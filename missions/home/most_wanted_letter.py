#!/usr/bin/env python3

"""
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.
"""


def main():
    """
    Take in input and run checkio
    :return:
    """

    i = input("Please enter a string: ")
    answer = checkio(i)
    print('"{0}"'.format(answer))
    quit()


def checkio(text):
    """
    Evaluate a given string to see which letter is the most common.

    :param text:
    :return most_frequent_letter:
    """
    letters = []

    # Evaluate if it's an alphanumeric
    for char in text.lower():
        if char.isalpha():
            letters.append(char)
    # print(letters)
    # quit()

    # Pop it from the list if it's a number
    for letter in letters:
        if letter.isdigit():
            letters.pop(letter)
    # print(letters)
    # quit()

    # Figure out the frequency of each letter
    import collections

    count = collections.Counter(letters)
    # print(count)

    # Grab the sorted list of most common
    most_common = count.most_common()
    # print(most_common)
    # quit()

    # Find the frequency of the most common letter:
    freq = most_common[0][1]

    # Drop the rest of the letters that appear less commonly
    index = len(most_common)
    for c in most_common:
        if c[1] == freq:
            continue
        else:
            # Find what index we're at
            # print(most_common.index(c))
            # quit()
            index = most_common.index(c)
            break

    # And slice the rest of the list off
    most_common = most_common[:index]
    # print(most_common)

    # If there's just one left, return it.
    if len(most_common) == 1:
        return most_common[0][0]

    # Find letter first alphabetically if there's more than one.
    most_common.sort()
    return most_common[0][0]


if __name__ == "__main__":
    main()
