"""
Daily Coding Problem - 2019-02-11.

Write a function that rotates a list by k elements. For example,
[1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2].

Try solving this without creating a copy of the list.
How many swap or move operations do you need?
"""


def solve(arr, k):
    """Given an array, rotate in by k elements."""
    if k > len(arr):
        return solve(arr, len(arr) - k)
    return arr[k:] + arr[:k]


print(solve([1, 2, 3, 4, 5, 6], 2))  # [3, 4, 5, 6, 1, 2]
