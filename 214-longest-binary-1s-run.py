"""
Daily Coding Problem - 2019-05-10.

Given an integer n, return the length of the longest consecutive run of 1s in
its binary representation.

For example, given 156, you should return 3.
"""


def solve(k):
    """Return the longest binary 1s run for the specified integer."""
    b = bin(k)[2:]
    run, max_run = 0, 0
    for i in b:
        if i == "0":
            run = -1
        run += 1
        max_run = max(run, max_run)
    return max_run


assert (solve(156)) == 3  # 10011100
assert (solve(3)) == 2  # 11
assert (solve(13)) == 2  # 1101
assert (solve(55)) == 3  # 110111
