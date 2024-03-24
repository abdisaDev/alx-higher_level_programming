#!/usr/bin/python3
def best_score(a_dictionary):
    max = (0, "")
    for x, y in a_dictionary.items():
        if y > max[0]:
            max = (y, x)
    return max[1]
