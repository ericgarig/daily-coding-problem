"""
Daily Coding Problem - 2019-04-18.

You are given an array of nonnegative integers. Let's say you start at the
beginning of the array and are trying to advance to the end. You can advance
at most, the number of steps that you're currently on. Determine whether you
can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1],
we can go from indices 0 -> 1 -> 3 -> 5, so return true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
"""


def solve(arr):
    """Determine if you can reach the final element in the array."""
    if len(arr) <= 1:
        return True
    for i in range(arr[0], 0, -1):
        if solve(arr[i:]):
            return True
    return False


assert solve([1, 3, 1, 2, 0, 1]) is True
assert solve([1, 2, 1, 0, 0]) is False
