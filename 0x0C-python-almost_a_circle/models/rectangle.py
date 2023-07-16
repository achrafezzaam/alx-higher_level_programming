#!/usr/bin/python3
'''Define the Rectangle class which inherits from the class Base'''
from .base import Base


class Rectangle(Base):
    '''Create a Rectangle Object inheriting from class Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''Instantiate the Rectangle object

        Args:
            width (int): The width of the Rectangle object
            height (int): The height of the Rectangle object
            x (int): The spaces number to add at the start of each line
            y (int): The newlines to add before the object representation
            id (int): The id of the Rectangle object
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''The width getter - Return the width of the Rectangle object'''
        return self.__width

    @width.setter
    def width(self, value):
        '''The width setter - Give a new width value to the
                              Rectangle object

        Args:
            value (int): The new width value
        '''
        self.error_handl("width", value, 0)
        self.__width = value

    @property
    def height(self):
        '''The height getter - Return the height of the Rectangle object'''
        return self.__height

    @height.setter
    def height(self, value):
        '''The height setter - Give a new height value to the
                               Rectangle object

        Args:
            value (int): The new height value
        '''
        self.error_handl("height", value, 0)
        self.__height = value

    @property
    def x(self):
        '''The x getter - Return the x value of the Rectangle object'''
        return self.__x

    @x.setter
    def x(self, value):
        '''The x setter - Give a new x value to the Rectangle object

        Args:
            value (int): The new x value
        '''
        self.error_handl("x", value, 1)
        self.__x = value

    @property
    def y(self):
        '''The y getter - Return the y value of the Rectangle object'''
        return self.__y

    @y.setter
    def y(self, value):
        '''The y setter - Give a new y value to the Rectangle object

        Args:
            value (int): The new y value
        '''
        self.error_handl("y", value, 1)
        self.__y = value

    def area(self):
        '''Return the area of the Rectangle object'''
        return self.__width * self.__height

    def display(self):
        '''Print the Rectangle to the stdout'''
        print("\n"*self.__y, end='')
        for i in range(self.__height):
            print(" "*self.__x+"#"*self.__width)

    def __str__(self):
        '''The Object representation when printed to stdout'''
        output = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.__x,
                                               self.__y, self.__width)
        if self.__class__.__name__ == 'Rectangle':
            output += "/{}".format(self.__height)
        return output

    def update(self, *args, **kwargs):
        '''Update the Rectangle values

        Args:
            *args (list): The new values in this order
                        <id> <width> <height> <x> <y>
            **kwargs (dict): A dictionary af new values used in case
                             *args is NULL or empty
        '''
        if len(args) == 0:
            for key, val in kwargs.items():
                setattr(self, key, val)
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.width = args[1]
        if len(args) > 2:
            self.height = args[2]
        if len(args) > 3:
            self.x = args[3]
        if len(args) > 4:
            self.y = args[4]

    def to_dictionary(self):
        '''Return a dictionary representation of the Object'''
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

    @staticmethod
    def error_handl(name, val, var):
        '''Error handler for the width, height, x and y values

        Args:
            name (str): the attribute name
            val (int): The attribute value
            var (int): Equal to 0 if name is width or height
                       and 1 if x or y
        Raises:
            TypeError: If val is not an integer
            ValueError: If the width or height are <= 0
                        or x or y are < 0
        '''
        if type(val) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if val <= 0 and var == 0:
            raise ValueError('{} must be > 0'.format(name))
        elif val < 0 and var == 1:
            raise ValueError('{} must be >= 0'.format(name))
