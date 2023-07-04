#!/usr/bin/python3
"""
Defining a Rectangle class
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        returns the value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the value of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        returns the value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        return the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)