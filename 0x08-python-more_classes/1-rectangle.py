#!/usr/bin/python3
"""
An class for rectangles
"""


class Rectangle:
    """A class representing a rectangle

    Attributes:
        __width (int): The width of the rectangle
        __height (int): The height of the rectangle

    Methods:
        width(self): Method to get the width attribute
        width(self, value): Method to set the width attribute
        height(self): Method to get the height attribute
        height(self, value): Method to set the height attribute
    """
    def __init__(self, width=0, height=0):
        """Initializing a square instance with an optional size and position

        Args:
            width (int, optional): The width of the rectangle
                                    which defaults to 0
            height (int, optional): The position of the rectangle
                                    which defaults to 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting the width attribute

        Returns:
            int: The width of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """Setting the width attribute

        Args:
            value (int): The width value to be assigned

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting the height attribute

        Returns:
            int: The height of the rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """Setting the height attribute

        Args:
            value (int): The height value to be assigned

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
