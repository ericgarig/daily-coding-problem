"""
Daily Coding Problem - 2019-04-27.

You are given an array of arrays of integers, where each array corresponds to a
row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents
the triangle:
  1
 2 3
1 5 1

We define a path in the triangle to start at the top and go down one row at a
time to an adjacent value, eventually ending with an entry on the bottom row.
For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
"""


def solve(arr):
    """Get the max weight of the path."""
    for i in range(len(arr) - 2, -1, -1):
        arr[i] = [max_subtriangle(arr, i, j) for j in range(len(arr[i]))]
    return arr[0][0]


def max_subtriangle(arr, top_row=0, top_index=0):
    """Given an array and the top point of a triangle, get the max sum."""
    max_bot = max(arr[top_row + 1][top_index], arr[top_row + 1][top_index + 1])
    return arr[top_row][top_index] + max_bot


assert (solve([[1], [2, 3], [1, 5, 1]])) == 9
