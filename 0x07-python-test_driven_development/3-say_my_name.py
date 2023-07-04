#!/usr/bin/python3
"""
This module contains a function that prints a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the person's name.

    Args:
        first_name (str): The person's first name.
        last_name (str, optional): The person's last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name or last_name:
        if last_name:
            print("My name is {} {}".format(first_name, last_name))
        else:
            print("My name is {}".format(first_name))
    else:
        print("My name is")
