#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lambdaF = lambda x: int(str.replace(str(x), str(search), str(replace)))
    return list(map(lambdaF, my_list))
