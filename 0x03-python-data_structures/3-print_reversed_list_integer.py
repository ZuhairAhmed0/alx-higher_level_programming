#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """ function that prints all integers of a list, in reverse order """
    my_list.reveres()
    for i in my_list:
        print("{:d}".format(i))
