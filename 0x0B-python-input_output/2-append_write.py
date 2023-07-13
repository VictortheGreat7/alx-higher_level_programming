#!/usr/bin/python3
"""
Module for the append_write function
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file (UTF8)
        and returns the number of characters added

    Args:
        filename: The name of the file where the string will be appended
        text: The string to be appended

    Returns:
        The number of characters added
    """
    with open(filename, 'a', encoding='utf=8') as file:
        return (file.write(text))
