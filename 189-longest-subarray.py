"""
Daily Coding Problem - 2019-04-15.

Given an array of elements, return the length of the longest subarray where all
its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest
subarray of distinct elements is [5, 2, 3, 4, 1].
"""


def solve(arr):
    """Return the length of the longest unique subarray."""
    max_len = 0
    for i, v in enumerate(arr):
        sub_arr = []
        for j in arr[v:]:
            if j not in sub_arr:
                sub_arr.append(j)
        max_len = max(max_len, len(sub_arr))
    return max_len


assert solve([5, 1, 3, 5, 2, 3, 4, 1]) == 5
assert solve([]) == 0
assert solve([1, 1, 1]) == 1
assert solve([1, 2, 1]) == 2
