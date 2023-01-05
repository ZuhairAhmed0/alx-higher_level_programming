#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    if len == 1:
        print("0 arguments.")
    elif len == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print(len - 1, "arguments:")
        for i in range(1, len):
            print("{}: {}".format(i, sys.argv[i]))
