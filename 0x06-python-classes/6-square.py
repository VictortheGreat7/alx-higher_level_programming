#!/usr/bin/python3
"""Square Class"""


class Square:
    """A class representing a square

    Attributes:
        __size (int): The size of the square
        __position (tuple): The position of the square

    Methods:
        area(self): Calculates and returns the current area of the square
        my_print(self): Prints in stdout the square with the character #

        size(self): Getter method to get the size attribute
        size(self, value): Setter method to set the size attribute
        position(self): Getter method to get the position attribute
        position(self, value): Setter method to set the position attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializing a square instance with an optional size and position

        Args:
            size (int, optional): The size of the square which defaults to 0
            position (tuple, optional): The position of the square
                                        which defaults to (0, 0)
        """
        self.__size = size
        self.position = position

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
        return (self.__size)

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

    @property
    def position(self):
        """Getting the position attribute

        Returns:
            tuple: The position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """Setting the position attribute

        Args:
            value (tuple): The position value to be assigned

        Raises:
            TypeError: If position is not a tuple of 2 positive integers
        """
        if (type(value) is not tuple) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Printing the square using the '#' character.

        If size is 0, it prints an empty line.
        Otherwise, it prints the square
        considering the position attribute
        and using '#' characters to represent it
        """
        if (self.__size == 0):
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
