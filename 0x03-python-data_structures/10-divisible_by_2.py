#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """ function that finds all multiples of 2 in a list. """
    new_list = my_list[:]
    idx = 0
    for i in my_list:
        if i % 2 == 0:
            new_list[idx] = True
        else:
            new_list[idx] = False
        idx += 1
    return new_list
