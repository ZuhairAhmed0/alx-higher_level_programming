#!/usr/bin/python3
def no_c(my_string):
    """ unction that removes all characters c and C from a string """
    noC = ""
    for ch in my_string:
        if ch != "C" and ch != "c":
            noC += ch
    return noC
