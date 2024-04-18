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
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Area method to return the are of the given square """
        return self.__size ** 2

    @property
    def size(self):
        """ Getter method for __size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method for __size attribute """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if (value < 0):
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        """ Print square based on __size """
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
