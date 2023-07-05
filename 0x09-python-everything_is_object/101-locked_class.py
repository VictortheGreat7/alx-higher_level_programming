#!/usr/bin/python3
"""A class with restricted attribute creation"""


class LockedClass:
    """A class that prevents the creation of new instance attributes,
    except for 'first_name'
    """

    __slots__ = ['first_name']

    def __init__(self):
        """Initializes a new instance of LockedClass"""
        pass
