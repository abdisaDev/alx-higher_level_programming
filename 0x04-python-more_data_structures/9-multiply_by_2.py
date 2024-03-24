#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    a = list(map(lambda x: x, a_dictionary))
    for x in a:
        new_dict[x] = a_dictionary[x] * 2
    return new_dict
