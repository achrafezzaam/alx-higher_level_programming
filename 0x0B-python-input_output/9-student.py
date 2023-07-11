#!/usr/bin/python3
'''Define the Student class'''


class Student:
    '''Create the student object'''
    def __init__(self, first_name, last_name, age):
        '''Instantiate the Student Object

        Args:
            first_name (str): The name of the Student instance
            last_name (str): The last name of the Student instance
            age (int): The age of the Student instance
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Retrieves a dictionary representation of the Student object'''
        return self.__dict__
