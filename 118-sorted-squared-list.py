"""
Daily Coding Problem - 2019-02-03.

Given a sorted list of integers, square the elements and give the output
in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""


def solve(arr):
    """Return a sorted squared array."""
    return sorted([i ** 2 for i in arr])


print(solve([-9, -2, 0, 2, 3]))  # [0, 4, 4, 9, 81]
