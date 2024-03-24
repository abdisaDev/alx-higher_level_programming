#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = sorted(list(map(lambda x: x ,a_dictionary.items())))
    for key in keys:
        print("{:s}: {}".format(key[0], key[1]))
