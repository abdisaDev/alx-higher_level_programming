#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for _ in range(0, len(my_list)):
        print(my_list.pop())
