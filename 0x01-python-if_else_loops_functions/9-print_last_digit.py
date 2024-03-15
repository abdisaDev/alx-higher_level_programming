#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    if number > 0:
        return f"{last_digit:d}{last_digit:d}"
    elif number <= 0:
        return f"{last_digit:d}{last_digit:d}"
