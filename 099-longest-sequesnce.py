"""
Daily Coding Problem - 2019-01-15.

Given an unsorted array of integers, find the length of the longest
consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2], the longest consecutive
element sequence is [1, 2, 3, 4]. Return its length: 4.
"""


def solve(arr):
    """Find the length of the longest consecutive sequence."""
    arr.sort()
    run = 0
    max_run = 0
    prev = arr[0] - 2    # some non-consecutive previous value
    for i in arr:
        if prev + 1 == i:
            run += 1
            prev = i
        else:
            if run > max_run:
                max_run = run
            run = 1
            prev = i
    return max_run


print(solve([100, 4, 200, 1, 3, 2]))    # 4
