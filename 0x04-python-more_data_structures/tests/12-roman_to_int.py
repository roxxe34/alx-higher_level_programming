#!/usr/bin/python3
def roman_to_int(s):
    if not (isinstance(s, str)) or s is None:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                  'M': 1000}
    rom_list = [roman_dict[char] for char in s]
    final_number = 0
    i = 0
    while(i < len(rom_list)):
        if roman_dict.get(s[i], 0) == 0:
            return (0)
        if i == len(rom_list) - 1:
            final_number += rom_list[i]
            break
        if rom_list[i] >= rom_list[i + 1]:
            final_number += rom_list[i]
            i += 1
        elif rom_list[i] < rom_list[i + 1]:
            final_number += rom_list[i + 1] - rom_list[i]
            i += 2
    return final_number
