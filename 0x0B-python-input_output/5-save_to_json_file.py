#!/usr/bin/python3
"""
Module for the save_to_json_file function
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation

    Args:
        filename: The name of the file to be written in
        my_obj: The object to be written
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
