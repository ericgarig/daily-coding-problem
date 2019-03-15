"""
Daily Coding Problem - 2019-03-12.

Given a list of elements, find the majority element, which appears more
than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.
"""


def solve(arr=[]):
    """Find majority element in a list."""
    d = {}
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return max(d, key=d.get)


assert (solve([1, 2, 1, 1, 3, 4, 0])) == 1
assert (solve([1, 2, 1, 2, 2])) == 2
