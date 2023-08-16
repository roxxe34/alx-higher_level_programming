#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sortdict = sorted(a_dictionary)
    for key in sortdict:
        print("{}: {}".format(key, a_dictionary[key]))
