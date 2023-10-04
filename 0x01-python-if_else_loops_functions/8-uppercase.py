#!/usr/bin/python3
# This is the  program that print string in "UPPERCASE", followed by newline


def uppercase(str):
    for c in str:
        if ord("a") <= ord(c) <= ord("z"):
            c = chr(ord(c) - 32)
        print("{:s}".format(c), end="")
    print()

