"""
Daily Coding Problem - 2019-02-03.

Given a set of closed intervals, find the smallest set of numbers that
covers all the intervals. If there are multiple smallest sets, return
any of them.

For example, given the intervals [0, 3], [2, 6], [3, 4], [6, 9], one set
of numbers that covers all these intervals is {3, 6}.
"""


def solve(arr=None):
    """Determine the smallest interval that covers each set."""
    if not arr:
        return None
    low = arr[0][1]
    high = arr[0][0]
    for i in arr:
        low = min(low, i[1])
        high = max(high, i[0])
    return {low, high}


print(solve([[0, 3], [2, 6], [3, 4], [6, 9]]))  # {3, 6}
