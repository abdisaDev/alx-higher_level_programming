#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total_val = 0
    for element in range(x):
        try:
            print(my_list[element], end="")
            total_val += 1
        except IndexError:
            pass
    print()
    return total_val
