#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dicts = {}
    for x, y in a_dictionary.items():
        new_dicts[x] = y * 2
    return new_dicts
