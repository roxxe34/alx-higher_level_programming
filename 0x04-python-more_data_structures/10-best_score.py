#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max = 0
    for k, v in a_dictionary.items():
        if v > max:
            max = v
            key = k
    return key
