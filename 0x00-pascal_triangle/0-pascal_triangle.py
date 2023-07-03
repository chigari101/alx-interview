#!/usr/bin/python3
"""
    function returns a list of lists of integers
    represents the Pascal’s triangle of n
    returns an empty list if n <= 0
    assumes n will be always an integer
"""


def pascal_triangle(n):
    """returns empty list if n <= 0"""
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = prev_row[j-1] + prev_row[j]
        triangle.append(row)
    return triangle
