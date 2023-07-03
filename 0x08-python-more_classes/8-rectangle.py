#!/usr/bin/python3
'''Define the Rectangle class'''


class Rectangle:
    '''Create a rectangle object

    Args:
        number_of_instances (int): number of created instances
        print_symbol (str): The string used to print the rectangle
    '''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''Instanciate the Rectangle object

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Retrieve the width value'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set a new value to the width

        Args:
            value (int): The new width of the rectangle instance
        '''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''Retrieve the height value'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set a new value to the height

        Args:
            value (int): The new height of the rectangle instance
        '''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''Compute the area of the rectangle instance'''
        return self.__width * self.__height

    def perimeter(self):
        '''Compute the perimeter of the rectangle instance'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''Return a rectangle to print'''
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["{}".format(self.print_symbol) * self.__width
                          for i in range(self.__height)])

    def __repr__(self):
        '''Return a string representation of the rectangle'''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''Print a message when an instance of Rectangle is deleted'''
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Return the biggest rectangle

        Args:
            rect_1 (Rectangle): The first rectangle to compare
            rect_2 (Rectangle): The second rectangle to compare
        '''
        if type(rect_1) != Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) != Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
