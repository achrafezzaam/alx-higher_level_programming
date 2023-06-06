#!/usr/bin/python3
def islower(c):
    '''
    # The islower function checks if the given variable c
    # is lowercase or not.
    #
    # This function should return True if c is lowercase
    # and False if not.
    '''
    c = ord(c)
    if c >= 97 and c <= 122:
        return True
    else:
        return False
