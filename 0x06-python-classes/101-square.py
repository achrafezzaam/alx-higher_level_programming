#!/usr/bin/python3
'''Define a Square'''


class Square:
    '''Create the Square object'''
    def __init__(self, size=0, position=(0, 0)):
        '''Instantiate the Square Object

        Args:
            size (int): the size of the Square object
            position (tuple): number of spaces to add at the
            beginning of the drawn square
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''Get the size of the Square object'''
        return self.__size

    @size.setter
    def size(self, value):
        '''Set the size of the Square object

        Args:
            value (int): The new value of the Square object's
            size value
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        '''Get the position value of the Square object'''
        return self.__position

    @position.setter
    def position(self, value):
        '''Set the position value of the Square object

        Args:
            value (tuple): number of spaces to add at the
            beginning of the drawn square
        '''
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''Compute the area of the Square object'''
        return self.__size ** 2

    def my_print(self):
        '''Print the Square object to the stdout'''
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")

    def __str__(self):
        '''Define the printed data at the object creation'''
        for i in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i != self.size - 1:
                print("")
        if self.__size == 0:
            print("")
        return ("")
