"""
Daily Coding Problem - 2019-01-06.

Given an integer n and a list of integers l, write a function that
randomly generates a number from 0 to n-1 that isn't in l (uniform).
"""
import random


def solve(n, l):
    """Return a random number not in the list."""
    choice_list = []
    for i in range(n):
        if i not in l:
            choice_list.append(i)
    if choice_list:
        return random.choice(choice_list)
    return None


print(solve(6, [0, 4]))    # 1, 2, or 3
print(solve(2, [0, 1, 2]))    # None
