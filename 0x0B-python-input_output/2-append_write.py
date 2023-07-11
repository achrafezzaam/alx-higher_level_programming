#!/usr/bin/python3
'''Define the append_write method'''


def append_write(filename="", text=""):
    '''Open the file filename, append text at the end then return
    the number of writen characters

    Args:
        filename (str): The file path
        text (str): The text to be appended
    '''
    with open(filename, "a", encoding="utf-8") as f:
        count = f.write(text)
    return count
