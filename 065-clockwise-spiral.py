"""
Daily Coding Problem - 2018-12-12.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,   2,  3,  4,  5],
 [6,   7,  8,  9, 10],
 [11, 12, 13, 14, 15],
 [16, 17, 18, 19, 20]]

You should print out the following ( return-delimitted ):

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
"""


def print_clockwise(arr):
    """Print an array in a clockwise spiral."""
    rows = range(len(arr) + 1)
    cols = range(len(arr[0]) + 1)
    while rows or cols:
        # left to right
        for i in rows:
            print(arr[cols[0]][i])

        # top to bottom
        # right to left
        # bottom to top
        # cols and rows decrease by 1 on both ends
    return True


# 1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12
arr = [[1, 2, 3, 4, 5],
       [6, 7, 8, 9, 10],
       [11, 12, 13, 14, 15],
       [16, 17, 18, 19, 20]]
print(print_clockwise(arr))
