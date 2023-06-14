#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) and roman_string is not None:
        rom = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        sign = 0
        temp = 0
        ans = 0
        roman_string = list(roman_string)
        roman_string.reverse()
        for elem in roman_string:
            if rom[elem] < temp or (rom[elem] == temp and sign != 0):
                ans -= rom[elem]
                sign = 1
            else:
                ans += rom[elem]
                temp = rom[elem]
                sign = 0
        return ans
    else:
        return 0
