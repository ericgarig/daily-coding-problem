"""
Daily Coding Problem - 2019-03-04.

Given a list, sort it using this method:
reverse(lst, i, j), which reverses lst from i to j.
"""


def solve(lst, i, j):
    """Reverse the specified list from index i to j."""
    if i < 0:
        return None
    if j >= len(lst):
        return None

    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst


assert (solve([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1, 2)) == [
    0,
    2,
    1,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
]
assert (solve([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], -1, 6)) == None
assert (solve([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9, 10)) == None
assert (solve([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 9)) == [
    9,
    8,
    7,
    6,
    5,
    4,
    3,
    2,
    1,
    0,
]
