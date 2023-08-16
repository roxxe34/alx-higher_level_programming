#!/usr/bin/python3
def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)) or roman_string is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    final_number = 0
    i = 0
    while(i < len(roman_string)):
        if roman_dict.get(roman_string[i], 0) == 0:
            return (0)
        if i == len(roman_string) - 1:
            final_number += roman_dict[roman_string[i]]
            break
        if roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
            final_number += roman_dict[roman_string[i]]
            i += 1
        elif roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]:
            final_number += roman_dict[roman_string[i + 1]] - roman_dict[roman_string[i]]
            i += 2
    return final_number
