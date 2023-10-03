#!/usr/bin/python3
# This is the  program that print string in "UPPERCASE", followed by newline
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
            print("")
