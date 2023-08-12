#!/usr/bin/python3
def no_c(my_string):
    new_str = list(my_string)
    for i in range(len(new_str)):
        if new_str[i] == "c" or new_str[i] == "C":
            new_str[i] = ""

    return "".join(new_str)
