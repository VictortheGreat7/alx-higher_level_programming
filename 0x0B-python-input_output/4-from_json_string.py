#!/usr/bin/python3
"""
Module for the from_json_string function
"""


import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: The JSON string

    Returns:
        The object that the JSON string represents
    """
    return (json.loads(my_str))
