"""
Daily Coding Problem - 2019-02-25.

Given an array of integers in which two elements appear exactly once and
all other elements appear exactly twice, find the two elements that
appear only once.

For example, given the array [2, 4, 6, 8, 10, 2, 6, 10], return 4 and 8.
The order does not matter.

Follow-up: Can you do this in linear time and constant space?
"""


def solve(arr=[]):
    """
    Return the two elements that appear only once.

    Brute force approach.
    """
    unique = []
    for i in arr:
        if i in unique:
            unique.remove(i)
        else:
            unique.append(i)
    return unique


def solve_linear_space_time(arr=[]):
    """Linear space and time solution to finding unique elements."""
    arr.sort()
    unique = []
    i = 0
    while i < len(arr):
        if len(arr) != i + 1 and arr[i] == arr[i + 1]:
            i += 1
        else:
            unique.append(arr[i])
        i += 1
    return unique


assert (solve([2, 4, 6, 8, 10, 2, 6, 10])) == [4, 8]
assert (solve_linear_space_time([2, 4, 6, 8, 10, 2, 6, 10])) == [4, 8]
