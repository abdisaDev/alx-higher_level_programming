#!/usr/bin/python3
def uppercase(str):
    "Function to change lowercase chars to upper"
    for char in str:
        charachter = None
        if ord(char) >= 97 and ord(char) <= 122:
            charachter = chr(ord(char) - 32)
        else:
            charachter = chr(ord(char))
        print("{:s}".format(charachter), end="")
    print("")
