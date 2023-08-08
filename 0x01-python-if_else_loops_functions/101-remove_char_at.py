#!/usr/bin/python3
def remove_char_at(str, n):
    char_list = list(str)
    if n <= len(char_list) and n >= 0:
        char_list[n] = ""
        new_string = ''.join(char_list)
        return new_string
    else:
        return str
