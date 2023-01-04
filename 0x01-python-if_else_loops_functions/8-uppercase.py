#!/usr/bin/python3
def uppercase(str):
    reslut = ""
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            reslut += chr(ord(ch) - 32)
        else:
            reslut += ch
    print("{}".format(reslut))
