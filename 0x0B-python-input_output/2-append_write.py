#!/usr/bin/python3
"""
Module for the write_file function
"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of characters written

    Args:
        filename: The name of the file to be written in
        text: The string to be written in the file
    """
    with open(filename, 'w', encoding='utf=8') as file:
        return file.write(text)
