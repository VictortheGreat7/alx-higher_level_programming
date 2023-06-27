#!/usr/bin/python3
"""Square Class"""


class Square:
    """A class representing a square

    Attributes:
        __size (int): The size of the square

    Methods:
        area(self): Calculates and returns the current area of the square
        size(self): Getter method to get the size attribute
        size(self, value): Setter method to set the size attribute
    """

    def __init__(self, size=0):
        """Initializing a square instance with an optional size

        Args:
            size (int, optional): The size of the square which defaults to 0
        """
        self.__size = size

    def area(self):
        """Calculating and returning the area of the square

        Returns:
            int: The area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """Getting the size attribute

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setting the size attribute

        Args:
            value (int): The size value to be assigned

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
