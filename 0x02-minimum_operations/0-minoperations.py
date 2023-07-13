#!/usr/bin/python3


"""
    In a text file, there is a single character H.
    The text editor can execute only two operations in this file:
    Given a number n, this a script that write a method that calculates the fewest number
    of operations needed to result in exactly n H characters in the file.
"""

def minOperations(n):
    if not isinstance(n, int) or n < 1:
        return 0

    ops_count = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            ops_count += divisor
            n //= divisor
        else:
            divisor += 1

    return ops_count
