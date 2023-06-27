#!/usr/bin/python3
"""Square Class"""


class Square:
    """A class Square with a private instance attribute: size"""

    def __init__(self, size):
        """Initializing a square instance

        Args:
            size (int): The size of the square
        """
        self.__size = size
