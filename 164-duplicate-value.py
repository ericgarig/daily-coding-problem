"""
Daily Coding Problem - 2019-03-20.

You are given an array of length n + 1 whose elements belong to the set
{1, 2, ..., n}. By the pigeonhole principle, there must be a duplicate.
Find it in linear time and space.
"""


def solve(arr):
    """Find the duplicate in linear time."""
    return sum(arr) - sum(set(arr))


assert (solve([1, 2, 3, 2])) == 2
assert (solve([1, 2, 3, 4, 5, 6, 6])) == 6
assert (solve([1, 6, 3, 4, 5, 6, 2])) == 6
