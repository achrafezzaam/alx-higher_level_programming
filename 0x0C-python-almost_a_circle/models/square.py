#!/usr/bin/python3
'''Define the Square class which insherits from the Rectangle class'''
from .rectangle import Rectangle


class Square(Rectangle):
    '''Create the Square object inheriting from the Rectangle class'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Instantiate the Square object

        Args:
            size (int): The size of the Square object
            x (int): The spaces number to add at the start of each line
            y (int): The newlines to add before the object representation
            id (int): The id of the Rectangle object
        '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''The size getter - Return the size of the Square object'''
        return self.width

    @size.setter
    def size(self, value):
        '''The size setter - Give a new size to the Square object

        Args:
            value (int): the new size value
        '''
        self.error_handl("width", value, 0)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''Update the Square values

        Args:
            *args (list): The new values in this order
                        <id> <size> <x> <y>
            **kwargs (dict): A dictionary af new values used in case
                             *args is NULL or empty
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                setattr(self, key, val)
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        '''Return a dictionary representation of the Object'''
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
