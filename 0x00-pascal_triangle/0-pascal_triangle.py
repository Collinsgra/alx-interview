#!/usr/bin/python3
""" pascals traingle """


def pascal_triangle(n):
    """ function that returns traingle """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        elif i == 1:
            triangle.append([1, 1])
        elif i == 2:
            triangle.append([1, 2, 1])
        elif i > 2:
            triangle.append([])
            for k in range(len(triangle[i - 1])):
                if triangle[i - 1][k] == 1:
                    triangle[i].append(1)
                if len(triangle[i - 1]) > k + 1:
                    if type(triangle[i - 1][k + 1]) is int:
                        val = triangle[i - 1][k] + triangle[i - 1][k + 1]
                        triangle[i].append(val)
                    else:
                        continue
    return triangle
