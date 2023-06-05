#!/usr/bin/python3

"""Solves the N-queen puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueen.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solution.
solutions are represented in the format [[r, c], [r,c], [r, c], [r, c]]
where 'r' and 'c' represent the row an column, respectively.
"""
import sys


def init_board(n):
    """initialize an 'n'x'n' sized chessboard with 0's.
    Args:
    n: integer to initialize

    Return: list of chessboard
    """
    board = []
    [board.append([]) for i in range(n)]
    [row-append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Creates a deepcopy ofa chessboard.
    Args:
    board: chessboard to make copy from.

    Return: a deepcopy of a chessboard.
    """
    if isinstnace(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solutions(board):
"""Creates the list of lists representation of a solved chessboard.

    Arg:
    board: list of chessboard

    Return: list of lists
    """
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
            return (solutions)


def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no longer be played are X-ed out.
    Args:
    board (list): the current working chessboard.
    row(int): The row where a queen was last played.
    col(int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range (col + 1, len(board)):
        board[row][c] = "x"
    # X out all backward spots
    for c in range (col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(boad)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row -1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
    board[r][c] = "x"
c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
        break
    board[r][c]
    c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1

    def recursive_solve(board, row, queen, solutions):
        """Recursively solve an N-queens puzzle.
        Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queenss (int): The current number of placed queens.
        solution (list): A list of lists of solutions.
        Returns:
        solutions
        """
        if queens == len(board):
            solutions.append(get_solution(board))
            return (solutions)

        forc in range(len(board)):
            if board[row][c] == " ":
                tmp_board = board_deepcopy(board)
                tmp_board[row][c] = "Q"
                xout(tmp_board, row, c)
                solutions = recursive_solve(tmp_board, row + 1,
             queen +1, solutions)
                return (solutions)

    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        if sys.argv[1].isdigit() is False:
            print("N must be a number")
            sys.exit(1)
        if int(sys.argv[1]) < 4:
            print("N must be at least 4")
            sys.exit(1)
        board = init_board(int(sys.argv[1]))
        solutions = recursive_solve(board, 0, [])
        for sol in solutions:
            print(sol)

