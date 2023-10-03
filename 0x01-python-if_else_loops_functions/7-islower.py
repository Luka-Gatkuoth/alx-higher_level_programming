#!/usr/bin/python3
# This is the program tha will check for lower case character
def islower(c):
    if ord(c) in range(97, 122):
        return True
    else:
        return False
