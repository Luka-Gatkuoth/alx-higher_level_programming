#!/usr/bin/python3
"""Module to find the max integers in the list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in the list of the integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return
