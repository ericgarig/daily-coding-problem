"""
Daily Coding Problem - 2019-06-10.

You are given an array of integers, where each element represents the
maximum number of steps that can be jumped going forward from that
element. Write a function to return the minimum number of jumps you
must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2,
as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.
"""


def solve(k=[]):
    """Get the min number of jumps to get thru the array."""
    if len(k) < 2:
        return 1
    min_jumps = len(k)
    for i in reversed(range(k[0])):
        if i > len(k):
            return 1
        if k[i] != 0:
            sub_jumps = solve(k[i + 1 :])
            min_jumps = min(min_jumps, sub_jumps)
    return min_jumps


assert solve([6, 2, 4, 0, 5, 1, 1, 4, 2, 9]) == 2
