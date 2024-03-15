#!/usr/bin/python3
def uppercase(str):
    "Function to change lowercase chars to upper"
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            print("{:s}".format(chr(ord(char) - 32)), end="")
    print("")