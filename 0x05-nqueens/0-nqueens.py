#!/usr/bin/python3
""" Module for Nqueens problem
"""


import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

# Check if n is valid
try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)

if n < 4:
    print("N must be at least 4")
    exit(1)

# Initialize all the needed sets and lists
cols = set()
posdiag = set()
negdiag = set()
result = []
board = [['.'] * n for _ in range(n)]


def backtrack(row):
    """
    Recursive backtracking function to find all the possible solutions
    for the Nqueens problem.
    """

    # Terminating Condition
    if row == n:
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'Q':
                    result.append([i, j])
        print(result)
        result.clear()
        return

    # Main logic to determin if a queen can be placed
    for col in range(n):
        if (col in cols) or (row + col in posdiag) or (row - col in negdiag):
            continue

        cols.add(col)
        posdiag.add(row + col)
        negdiag.add(row - col)
        board[row][col] = 'Q'

        backtrack(row + 1)

        cols.remove(col)
        posdiag.remove(row + col)
        negdiag.remove(row - col)
        board[row][col] = ' '


backtrack(0)
