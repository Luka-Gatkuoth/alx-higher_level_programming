#!/usr/bin/python3
# This is the  program that print string in "UPPERCASE", followed by newline
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
        print("")
