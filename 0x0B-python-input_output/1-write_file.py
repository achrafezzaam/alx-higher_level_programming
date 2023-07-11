#!/usr/bin/python3
'''Define the write_file method'''


def write_file(filename="", text=""):
    '''Write text to file filename

    Args:
        filename (str): The file\'s path
        text (str): The text to be writen in the file
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        count = f.write(text)
    return count
