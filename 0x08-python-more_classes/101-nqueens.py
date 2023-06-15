#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    def backtrack(board, row, columns):
        if row == n:
            # Found a valid solution
            solutions.append([[i, columns[i]] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                columns.append(col)  # Track the column index
                backtrack(board, row + 1, columns)
                board[row][col] = '.'
                columns.pop()  # Remove the column index

    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    backtrack(board, 0, [])  # Pass an empty list for columns

    for solution in solutions:
        print(solution)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        solve_nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
