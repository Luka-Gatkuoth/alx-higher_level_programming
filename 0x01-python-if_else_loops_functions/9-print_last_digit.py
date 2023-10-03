#!/usr/bin/python3
# Program that print last digit of the given number
def print_last_digit(number):
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
