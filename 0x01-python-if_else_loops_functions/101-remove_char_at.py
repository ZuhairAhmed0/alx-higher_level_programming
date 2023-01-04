#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for ch in str:
        if n >= 0 and n < len(str):
            if ch == str[n]:
                continue
        result += ch
    return result
