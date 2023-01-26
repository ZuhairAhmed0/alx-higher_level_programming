#!/usr/bin/python3
# 2-square.py
"""Define a class Square."""


class Square:
    """size must be an integer, otherwise raise a TypeError
    if size is less than 0, raise a ValueError
    exception with the message size must be >= 0"""
    def __init__(self, size=0):
        self.__size = size

    # This function return size
    @property
    def size(self):
        return self.__size

    # this function change the size to new value
    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # that returns the current square area
    def area(self):
        return self.__size**2

    # that prints in stdout the square with the character #
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print(self.__size * "#")
