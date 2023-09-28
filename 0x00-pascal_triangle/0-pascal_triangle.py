#!/usr/bin/python3
"""
A module for Pascal's Triangle.
"""

def pascal_triangle(n):
    if type(n) is not int or  n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # The first element of each row is always 1
        if i > 0:
            # Calculate the rest of the row based on the previous row
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # The last element of each row is always 1
        triangle.append(row)

    return triangle
