#!/usr/bin/python3
for ch in range(90, 64, -2):
    print("{}{}".format(chr(ch + 32), chr(ch - 1)), end="")
