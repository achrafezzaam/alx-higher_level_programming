#!/usr/bin/python3
def no_c(my_string):
    c = 0
    while c < len(my_string):
        if my_string[c] == 'c' or my_string[c] == 'C':
            my_string = my_string[:c] + my_string[c+1:]
            c -= 1
        c += 1
    return my_string
