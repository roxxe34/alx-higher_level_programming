#!/usr/bin/python3
def remove_char_at(str, n):
    char_list = list(str)
    char_list[n] = ""
    new_string = ''.join(char_list)
    return new_string
