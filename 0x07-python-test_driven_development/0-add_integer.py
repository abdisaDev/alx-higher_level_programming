#!/usr/bin/python3

""" Two Number Adding Module """


def add_integer(a, b=98):
    """ Two Number Adding Function """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")
