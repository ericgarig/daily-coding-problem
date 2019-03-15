"""
Daily Coding Problem - 2019-02-07.

You are given a 2-d matrix where each cell represents number of coins in
that cell. Assuming we start at matrix[0][0], and can only move right or
down, find the maximum number of coins you can collect by the bottom
right corner.

For example, in this matrix
0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""


def solve(arr=[]):
    """Find the max value of iterating thru 2D matrix by moving left/down."""
    if not arr:
        return 0
    if len(arr[0]) == 1:
        return arr[0][0]
    try:
        move_left = solve(arr[1:])
    except IndexError:
        move_left = 0
    try:
        move_down = solve([i[1:] for i in arr])
    except IndexError:
        move_down = 0
    return arr[0][0] + max(move_left, move_down)


arr = [[0, 3, 1, 1], [2, 0, 0, 4], [1, 5, 3, 1]]
assert (solve(arr)) == 12
