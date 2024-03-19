#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for index in range(1, len(sys.argv)):
        sum += int(index)
    print(sum)
