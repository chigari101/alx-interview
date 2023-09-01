#!/usr/bin/python3

"""0x09. Island Perimeter """


def island_perimeter(grid):
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                # Start with the assumption that its a land cell

                # Check neighboring cells (up, down, left, right)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 if there's land to the north
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 if there's land to the west

    return perimeter
