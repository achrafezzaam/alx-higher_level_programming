#!/usr/bin/python3
'''Define the class_to_json method'''


def class_to_json(obj):
    '''Return an object\'s arguments as a dictionary'''
    return obj.__dict__
