#!/usr/bin/python3
def multiple_returns(sentence):
    """ function that returns a tuple with the length of a string
    and its first character """
    first = "None"
    lens = len(sentence)
    if lens != 0:
        first = sentence[0]

    return lens, first
