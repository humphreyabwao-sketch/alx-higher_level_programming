#!/usr/bin/python3
# 6-print_comb3.py

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
    for digit1 in range(0, 9):
        for digit2 in range(digit1 + 1, 10):
            print("{}{}".format(digit1, digit2), end=", ")

print("89")
