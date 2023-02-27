#!/usr/bin/python3
""" MyList that inherits from list """

class MyList(list):
    """ sorted function """
    def print_sorted(self):
        """ Implements sorted """
        print(sorted(self))
