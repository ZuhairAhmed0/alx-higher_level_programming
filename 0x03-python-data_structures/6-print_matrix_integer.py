#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """ function that prints a matrix of integers. """
    for col in matrix:
        for row in col:
            print("{:d}".format(row), end="")
            if row != col[-1]:
                print(end=" ")
        print()
