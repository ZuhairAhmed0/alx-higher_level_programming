#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len = len(sys.argv)
    if len == 1:
        print("0 arguments.")
    else:
        print(len - 1, "arguments:")
        for i in range(1, len):
            print(f"{i}: {sys.argv[i]}")
