#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sumList = 0
    sumTuple = 0
    for item in my_list:
        sumList += item[0] * item[1]
        sumTuple += item[1]
    return sumList / sumTuple
