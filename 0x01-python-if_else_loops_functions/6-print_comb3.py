#!/usr/bin/python3
for num_1 in range(0, 9):
    for num_2 in range(1, 10):
        if num_1 == num_2:
            continue
        elif num_1 == 8 and num_2 == 9:
            print("{:d}{:d}".format(num_1, num_2))
        else:
            print("{:d}{:d}".format(num_1, num_2), end=", ")