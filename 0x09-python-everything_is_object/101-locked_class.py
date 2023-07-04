#!/usr/bin/python3
'''Define the LockedClass class'''


class LockedClass:
    '''Create the LockedClass class which blocks the dynamic creation
    of instance attributes except for first_name'''
    __slots__ = "first_name"
