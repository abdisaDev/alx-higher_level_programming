#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for y in matrix:
        for x in y:
            if y.index(x) != len(y) - 1:
                print("{:d} ".format(x), end="")
            else:
                print("{:d}".format(x), end="")
        print()
