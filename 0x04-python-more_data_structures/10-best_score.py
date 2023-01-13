#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    best = sorted(list(a_dictionary.values()))
    best.reverse()
    for i, x in a_dictionary.items():
        if x == best[0]:
            return i
