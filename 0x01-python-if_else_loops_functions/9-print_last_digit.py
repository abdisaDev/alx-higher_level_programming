#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    if number > 0:
        print(f"{last_digit:d}", end="")
        return f"{last_digit:d}"
    elif number <= 0:
        print(f"{last_digit:d}", end="")
        return f"{last_digit:d}"
