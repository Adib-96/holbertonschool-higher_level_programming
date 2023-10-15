#!/usr/bin/python3

def add_integer(a, b=98):
    """"Add integer a to b in normal case.
    
    ----float args are typecasted to integer
    
    Raises:
        - TypeError: if either arguments is non-integer and non-float

    """
    if ((not isinstance(a,int) and not isinstance(a,float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b,int) and not isinstance(b,float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
