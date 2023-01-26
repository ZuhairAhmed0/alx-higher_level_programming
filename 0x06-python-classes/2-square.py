#!/usr/bin/python3
# 2-square.py
"""Define a class Square."""


class Square:
    """size must be an integer, otherwise raise a TypeError
    if size is less than 0, raise a ValueError
    exception with the message size must be >= 0"""
    def __init__(self, size=0):
        self.__size = size
        if not type(self.__size) is int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
