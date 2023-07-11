#!/usr/bin/python3
"""This module defines a Pascal's Triangle function"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n
      """
    if n <= 0:
        return []
    tri = [[1]]
    while len(tri) != n:
        t = tri[-1]
        temp = [1]
        for i in range(len(tri) - 1):
            temp.append(t[i] + t[i + 1])
        temp.append(1)
        tri.append(temp)
    return tri
