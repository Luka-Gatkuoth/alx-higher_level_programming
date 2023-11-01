#!/usr/bin/python3

"""Define the integer of addition function."""




def add_integer(a, b=98):
    """Return the integer addition of the a and b.
    Float arguments are typecasted into int before addition is performed.
    Raises:
    TypeError: If either of a or b is the non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

