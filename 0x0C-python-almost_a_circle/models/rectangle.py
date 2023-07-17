#!/usr/bin/python3
"""
    contains class Rectangle which implements Base.
"""
from .base import Base


class Rectangle(Base):
    """
       class Rectangle implements Base.
       Methods:
       __init__()
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
           Initializes the instance of the class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Getter and setter for width
    @property
    def width(self):
        """
           getter function for __width
           Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter function for width.
            Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Getter and setter for height
    @property
    def height(self):
        """
            getter function for height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for height
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    # Getter and setter for x
    @property
    def x(self):
        """
            getter function for x.
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter function for x.
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    # Getter and setter for y
    @property
    def y(self):
        """
            getter function for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter function for y
            Args:
                value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            returns the area of the Rectangle instance.
        """
        return self.__width * self.__height

    def display(self):
        """
        prints to stdout the Rectangle instance with '#'
        """
        print("\n" * self.__y, end="")
        for _ in range(self.height):
            for _ in range(self.x):
                print(' ', end="")
            for _ in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """
        returns a string format of the rectangle
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.x, self.y, self.__width,
                                                self.__height)

    def update(self, *args, **kwargs):
        """
        assigns key/value argument to attributes
        kwargs is skipped if args is not empty
        Args:
        *args -  variable number of no-keyword args
        **kwargs - variable number of keyword args
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
        returns the dictionary repr of a rectangle
        """
        # return {
        #     "x": self.x,
        #     "y": self.y,
        #     "id": self.id,
        #     "height": self.height,
        #     "width": self.width
        # }
        return {
            "x": self.x,
            "width": self.width,
            "id": self.id,
            "height": self.height,
            "y": self.y

        }
