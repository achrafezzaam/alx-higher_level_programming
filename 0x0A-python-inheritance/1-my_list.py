#!/usr/bin/python3
'''Define the MyList class'''


class MyList(list):
    '''Create the class MyList inheriting from list'''
    def print_sorted(self):
        '''Print the list sorted'''
        print(sorted(self))
