#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = list(filter(lambda x: x if x not in set_2 else "",set_1))
    b = list(filter(lambda y: y if y not in set_1 else "",set_2))
    a.extend(b)
    return a
