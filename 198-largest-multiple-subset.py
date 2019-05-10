"""
Daily Coding Problem - 2019-04-24.

Given a set of distinct positive integers, find the largest subset such that
every pair of elements in the subset (i, j) satisfies either
i % j = 0 or j % i = 0.

For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20].
Given [1, 3, 6, 24], return [1, 3, 6, 24].
"""


def solve(arr):
    """Find the largest subset of multiples."""
    arr.sort(reverse=True)
    exit_at = arr[-1]
    max_subset = []
    for i in range(len(arr)):
        if arr[i] <= exit_at:
            break
        current_subset = [
            arr[j] for j in range(i, len(arr)) if arr[i] % arr[j] == 0
        ]
        if len(max_subset) < len(current_subset):
            exit_at = max(exit_at, current_subset[1])
            max_subset = current_subset
            max_subset.sort()
    return max_subset


assert (solve([3, 5, 10, 20, 21])) == [5, 10, 20]
assert (solve([1, 3, 6, 24])) == [1, 3, 6, 24]
