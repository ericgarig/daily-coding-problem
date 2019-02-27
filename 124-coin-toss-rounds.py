"""
Daily Coding Problem - 2019-02-09.

You have n fair coins and you flip them all at the same time. Any that
come up tails you set aside. The ones that come up heads you flip again.
How many rounds do you expect to play before only one coin remains?

Write a function that, given n, returns the number of rounds you'd expect
to play until one coin remains.
"""

import random


def solve(n=0):
    """Given n coins, return the number of rounds you expect to play."""
    if n <= 1:
        return 0
    return solve(sum([random.randint(0, 1) for i in range(n)])) + 1


print(solve(10))
