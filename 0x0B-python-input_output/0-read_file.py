#!/usr/bin/python3
"""
Module for the read_file function
"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

    Args:
        filename: The name of the file to be read
    """
    with open(filename, 'r', encoding='utf=8') as file:
        print(file.read(), end="")
