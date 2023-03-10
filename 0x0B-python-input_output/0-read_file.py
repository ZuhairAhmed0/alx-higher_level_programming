#!/usr/bin/python3
""" 0-read_file.py """


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, encoding="utf-8") as fs:
        print(fs.read(), end="")
