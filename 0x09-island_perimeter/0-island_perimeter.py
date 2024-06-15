#!/usr/bin/python3
"""Island Perimeter technical interview question"""


def island_perimeter(grid):
    """Solution"""
    edges = 0
    cells = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                cells += 1
                if y > 0 and grid[y - 1][x] == 1:
                    edges += 1
                if x > 0 and grid[y][x - 1] == 1:
                    edges += 1
    return (cells * 4) - (edges * 2)
