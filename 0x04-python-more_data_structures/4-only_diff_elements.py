#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return list(filter(lambda x: x == "",
                       list(map(lambda x: x if x in set_2 else "", set_1))))
