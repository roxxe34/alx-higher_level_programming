#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for k, v in a_dictionary.items():
        new_dictionary[k] = a_dictionary[v] * 2
