"""
Daily Coding Problem - 2019-02-14.

Given a real number n, find the square root of n.
For example, given n = 9, return 3.
"""


def solve(n=0):
    """Find the square root of a number."""
    return n ** 0.5


assert (solve(9)) == 3
assert (solve(4)) == 2
assert (solve(2)) == 1.4142135623730951
assert (solve(-1)) == (6.123233995736766e-17 + 1j)
assert (solve(10000)) == 100
