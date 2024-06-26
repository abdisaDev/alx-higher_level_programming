#!/usr/bin/python3
""" Define a class Square """


class Square:
    """ Represent class Square """
    def __init__(self, size=0):
        """
            Initalize constructor for class Square
            with default size attribute (0)
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
