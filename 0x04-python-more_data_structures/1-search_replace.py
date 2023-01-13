#!/usr/bin/python3
def search_replace(my_list, search, replace):
    s = str(search)
    r = str(replace)
    return list(map(lambda x: int(str.replace(str(x), s, r)), my_list))
