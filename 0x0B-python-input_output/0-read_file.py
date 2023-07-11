#!/usr/bin/python3
'''Define the read_file method'''


def read_file(filename=""):
    '''Read a file and print it\'s content'''
    with open(filename, encoding='utf-8') as f:
        data = f.read()
        print(data, end="")
