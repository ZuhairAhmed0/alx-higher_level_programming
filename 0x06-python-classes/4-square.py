#!/usr/bin/python3
# 2-square.py
"""Define a class Square."""


class Square:
    """size must be an integer, otherwise raise a TypeError
    if size is less than 0, raise a ValueError
    exception with the message size must be >= 0"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size**2
