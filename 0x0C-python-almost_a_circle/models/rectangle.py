#!/usr/bin/python3
'''Define the Rectangle class which inherits from the class Base'''
from .base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.error_handl("width", value, 0)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.error_handl("height", value, 0)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.error_handl("x", value, 1)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.error_handl("y", value, 1)
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        print("\n"*self.__y, end='')
        for i in range(self.__height):
            print(" "*self.__x+"#"*self.__width)

    def __str__(self):
        output = "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                               self.id, self.__x,
                                               self.__y, self.__width)
        if self.__class__.__name__ == 'Rectangle':
            output += "/{}".format(self.__height)
        return output

    def update(self, *args, **kwargs):
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
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

    @staticmethod
    def error_handl(name, val, var):
        if type(val) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if val <= 0 and var == 0:
            raise ValueError('{} must be > 0'.format(name))
        elif val < 0 and var == 1:
            raise ValueError('{} must be >= 0'.format(name))
