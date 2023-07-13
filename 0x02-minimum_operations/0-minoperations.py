#!/usr/bin/python3


"""
    In a text file, there is a single character H.
    The text editor can execute only two operations in this file:
    Given a number n, this a script that write a method that calculates the fewest number
    of operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    if not isinstance(n, int):
        return 0

    nope = 0
    minope = 2
    while n > 1:
        while n % minope == 0:
            nope += minope
            n //= minope
        minope += 1
    return nope
