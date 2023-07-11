#!/usr/bin/python3
'''Define the load_from_json_file method'''
import json


def load_from_json_file(filename):
    '''Turn the content of a file into an object

    Args:
        filename (str): The path to the file
    '''
    with open(filename, mode="r", encoding='utf-8') as f:
        obj = json.load(f)
    return obj
