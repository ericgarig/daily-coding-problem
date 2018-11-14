"""
Daily Coding Problem - 2018-11-14.

You have an N by N board. Write a function that, given N, returns the
number of possible arrangements of the board where N queens can be
placed on the board without threatening each other, i.e. no two queens
share the same row, column, or diagonal.
"""
import copy


def main(board_size=0):
    """Given an N x N board, get the number of ways N-queens can be placed."""
    if board_size < 4:
        return 0
    board = create_board(board_size)
    global solutions
    solutions = []
    solve(board, 0)
    print_solutions(solutions)
    return len(solutions)


def create_board(board_size):
    """Create an N x N board."""
    board = [0] * board_size
    for col in range(board_size):
        board[col] = [0] * board_size
    return board


def print_board(board):
    """Print one board."""
    for row in board:
        print(row)


def print_solutions(solutions):
    """Pretty print the board."""
    for board in solutions:
        print_board(board)
        print('---')


def solve(board, col):
    """Find a solution for a board, using backtracking."""
    board_size = len(board)
    for i in range(board_size):
        if is_safe(board, i, col):
            board[i][col] = 1
            if col == (board_size - 1):
                solutions.append(copy.deepcopy(board))
                board[i][col] = 0
                return True
            solve(board, (col + 1))
            # now backtrack
            board[i][col] = 0


def is_safe(board, place_row, place_col):
    """Check if the queen placed at location on a board is safe."""
    board_size = len(board)
    for i in range(board_size):
        # check all other columns in the row
        if place_col != i:
            if board[place_row][i] == 1:
                return False
        # check all other rows in column
        if place_row != i:
            if board[i][place_col] == 1:
                return False

    # check diagonals - lower-right
    test_row = place_row + 1
    test_col = place_col + 1
    while True:
        if test_col >= board_size or test_row >= board_size:
            break
        if board[test_row][test_col] == 1:
            return False
        test_col += 1
        test_row += 1

    # check diagonals - upper-left
    test_row = place_row - 1
    test_col = place_col - 1
    while True:
        if test_col < 0 or test_row < 0:
            break
        if board[test_row][test_col] == 1:
            return False
        test_col -= 1
        test_row -= 1

    # check diagonals - lower-left
    test_row = place_row + 1
    test_col = place_col - 1
    while True:
        if test_col < 0 or test_row >= board_size:
            break
        if board[test_row][test_col] == 1:
            return False
        test_col -= 1
        test_row += 1

    # check diagonals - upper-right
    test_row = place_row - 1
    test_col = place_col + 1
    while True:
        if test_col >= board_size or test_row < 0:
            break
        if board[test_row][test_col] == 1:
            return False
        test_col += 1
        test_row -= 1
    return True


print(main(5))
