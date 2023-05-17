#!/usr/bin/python3
"""defines a ocked class"""

class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything except attributes called first_name
    """
    __slots__ = ["first_name"]
