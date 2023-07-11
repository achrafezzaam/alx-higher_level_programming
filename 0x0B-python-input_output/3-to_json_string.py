#!/usr/bin/python3
'''Define the to_json_string method'''
import json


def to_json_string(my_obj):
    '''Return an object in a json format

    Args:
        my_obj : The object to be transformed into a json'''
    return json.dumps(my_obj)
