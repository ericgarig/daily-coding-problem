"""
Daily Coding Problem - 2019-02-14.

Given a real number n, find the square root of n.
For example, given n = 9, return 3.
"""


def solve(n=0):
    """Find the square root of a number."""
    return n ** 0.5


print(solve(9))  # 3
print(solve(4))  # 2
print(solve(2))  # 1.4142...
print(solve(-1))  #
print(solve(10000))  # 100
