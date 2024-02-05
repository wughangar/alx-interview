#!/usr/bin/python3
""" 0. Island Perimeter """


def island_perimeter(grid):
    """
    function that returns the perimeter of the island dscrived in grid
    args:
        grid - list of integers
    """
    if not grid or not grid[0]:
        return 0
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
    return perimeter
