#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_of_my_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return copy_of_my_list
    else:
        copy_of_my_list[idx] = element
        return copy_of_my_list
