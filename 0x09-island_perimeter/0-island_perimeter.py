#!/usr/bin/python3
""" iSLAND PERIMETER"""


def island_perimeter(grid):
    """ i- perimeter func """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for p in range(cols):
            if grid[i][p] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][p] == 1:
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][p] == 1:
                    perimeter -= 1
                if p > 0 and grid[i][p - 1] == 1:
                    perimeter -= 1
                if p < cols - 1 and grid[i][p + 1] == 1:
                    perimeter -= 1

    return perimeter
