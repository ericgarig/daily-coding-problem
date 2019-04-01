"""
Daily Coding Problem - 2019-03-25.

Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

you should return:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Follow-up: What if you couldn't use any extra space?
"""


def solve(arr):
    """Rotate a matrix clockwise."""
    size = len(arr)
    for x in range(0, int(size / 2)):
        for y in range(x, size - x - 1):
            temp = arr[size - y - 1][x]
            arr[size - y - 1][x] = arr[size - x - 1][size - y - 1]
            arr[size - x - 1][size - y - 1] = arr[y][size - x - 1]
            arr[y][size - x - 1] = arr[x][y]
            arr[x][y] = temp
    return arr


assert (solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) == [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
]
