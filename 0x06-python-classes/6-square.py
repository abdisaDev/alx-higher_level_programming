#!/usr/bin/python3
""" Define a class Square """


class Square:
    """ Represent class Square """
    def __init__(self, size=0, position=(0, 0)):
        """
            Initalize constructor for class Square
            with default size attribute (0)
        """
        self.size = size
        self.position = position

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
                print(" " * self.__position[0], end="")
                for y in range(self.__size):
                    print(" " * self.__position[1], end="")
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
            if value[0] + value[1] < 1:
                raise TypeError("position must be a tuple of 2 positive integers")
            else:
                self.__position = value

mysquare = Square(3)
mysquare.my_print()
