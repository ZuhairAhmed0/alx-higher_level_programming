#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ function that prints all integers of a list, in reverse order """
#for i in range(len(my_list) - 1, -1, -1)
    rev = my_list[::-1]
    for i in rev:
        print("{:d}".format(i))
