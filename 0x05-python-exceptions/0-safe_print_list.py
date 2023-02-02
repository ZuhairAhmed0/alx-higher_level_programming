#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        size = 0
        for i in range(x):
            print(my_list[i], end="")
            size = size + 1
    except Exception:
        pass
    print()
    return size
