#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = list(map(lambda x: x, a_dictionary))
    for x in a:
        a_dictionary[x] *= 2
    return a_dictionary
