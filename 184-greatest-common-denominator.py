"""
Daily Coding Problem - 2019-04-10.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14.
"""


def solve(arr):
    """Find the greatest common denominator in a list."""
    for gcd in range(min(arr), 0, -1):
        for i in arr:
            if i % gcd != 0:
                break
        else:
            return gcd


assert (solve([42, 56, 14])) == 14
assert (solve([42, 56, 15])) == 1
