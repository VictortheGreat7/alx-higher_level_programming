#!/usr/bin/python3
"""Square Class"""


class Square:
    """A class representing a square

    Attributes:
        __size (int): The size of the square

    Methods:
        area(self): Calculates and returns the current area of the square
    """

    def __init__(self, size=0):
        """Initializing a square instance with an optional size

        Args:
            size (int, optional): The size of the square which defaults to 0
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculating and returning the area of the square

        Returns:
            int: The area of the square
        """
        return (self.__size ** 2)
