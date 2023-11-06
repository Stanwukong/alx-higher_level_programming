#!/usr/bin/python3
"""Solves the N queens problem."""

import sys

def is_safe(board, row, col, n):
    for i in range(col):
        if board[i] == row or board[i] - i == row - col or board[i] + i == row + col:
            return False
    return True

def solve_n_queens_util(board, col, n):
    if col == n:
        print([[i, board[i]] for i in range(n)])
        return True
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[col] = i
            res = solve_n_queens_util(board, col + 1, n) or res
    return res

def solve_n_queens(n):
    board = [-1 for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("No solution exists")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            raise ValueError("N must be at least 4")
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(N)

