#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        return {x: 2 * y for x, y in a_dictionary.items()}
