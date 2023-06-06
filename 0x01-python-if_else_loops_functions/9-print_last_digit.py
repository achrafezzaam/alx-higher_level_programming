#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
    last_dgt = number % 10
    print("{}".format(last_dgt), end="")
    return last_dgt
