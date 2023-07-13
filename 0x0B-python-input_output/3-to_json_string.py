#!/usr/bin/python3
"""
Module for the to_json_string function
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj: The object string

    Returns:
        The JSON representation of the object string
    """
    return (json.dumps(my_obj))
