#!/usr/bin/python3
def magic_string():
    magic_string.p = getattr(magic_string, 'p', 0) + 1
    return ("BestSchool, " * (magic_string.p - 1) + "BestSchool")
