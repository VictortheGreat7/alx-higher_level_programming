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
        area(self): Calculates and returns the rectangle's area
        perimeter(self): Calculates and returns the rectangle's perimeter

        width(self): Method to get the width attribute
        width(self, value): Method to set the width attribute
        height(self): Method to get the height attribute
        height(self, value): Method to set the height attribute

        number_of_instances (int): The number of instances of
                                    the class Rectangle
        print_symbol (any): The symbol used for string representation
                            of the rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing a square instance with an optional width and height

        Args:
            width (int): The width of the rectangle
                            which defaults to 0
            height (int): The position of the rectangle
                            which defaults to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a string representation of the rectangle

        Returns:
            str: The rectangle representation with the print_symbol characters
        """
        if (self.__width == 0) or (self.__height == 0):
            return ("")
        symbol = str(self.print_symbol)
        return ('\n'.join([symbol * self.__width
                for _ in range(self.__height)]))

    def __repr__(self):
        """Returns a string representation of the rectangle
            that can be used to recreate a new instance

        Returns:
            str: A string representation of the rectangle
        """
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted
            and decrements the instance count
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

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

    def area(self):
        """
        Calculates the area of the rectangle

        Returns:
            int: The area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle

        Returns:
            int: The perimeter of the rectangle
        """
        if (self.__width == 0) or (self.__height == 0):
            return (0)
        else:
            return (2 * (self.__width + self.__height))
