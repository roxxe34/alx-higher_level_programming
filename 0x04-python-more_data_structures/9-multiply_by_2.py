#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_to_remove = []
    for k, v in a_dictionary.items():
        if v == value:
            keys_to_remove.append(k)
    for key in keys_to_remove:
        a_dictionary.pop(key)

    return a_dictionary
