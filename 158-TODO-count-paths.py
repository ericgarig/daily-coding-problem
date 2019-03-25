"""
Daily Coding Problem - 2019-03-13.

You are given an N by M matrix of 0s and 1s. Starting from the top left
corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1
represents a wall you cannot walk through.

For example, given the following matrix:

[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]

Return two, as there are only two ways to get to the bottom right:
Right, down, down, right
Down, right, down, right

The top left corner and bottom right corner will always be 0.
"""


"""
NOT DONE.
NOT DONE.
NOT DONE.
"""


def solve(arr=[], pos=[0, 0]):
    """Count the number of ways to get from top-left to bottom-right."""
    ways = 0
    arr_height = len(arr) - 1
    arr_width = len(arr[0]) - 1
    while pos != [arr_height, arr_width]:
        if (pos[1] + 1) <= arr_width and arr[pos[0]][pos[1] + 1] == 0:
            ways += solve(arr, [pos[0], pos[1] + 1])
            pos = [pos[0], pos[1] + 1]
        if (pos[0] + 1) <= arr_height and arr[pos[0] + 1][pos[1]] == 0:
            ways += solve(arr, [pos[0] + 1, pos[1]])
            pos = [pos[0] + 1, pos[1]]
    else:
        return ways
    return ways


# assert (solve([[0, 0, 1], [0, 0, 1], [1, 0, 0]])) == 2
print(solve([[0, 0, 1], [0, 0, 1], [1, 0, 0]]))
