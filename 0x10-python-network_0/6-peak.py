#!/usr/bin/python3
""" Module that contains a function that finds a peak in a list of unsorted
    integers """

def find_peak(list_of_integers):
    sorted_list = sorted(list_of_integers)
    if len(sorted_list) == 0:
        return None
    return sorted_list[-1]
