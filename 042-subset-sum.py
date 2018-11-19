"""
Daily Coding Problem - 2018-11-18.

Given a list of integers S and a target number k, write a function that
returns a subset of S that adds up to k. If such a subset cannot be made,
then return null.

Integers can appear more than once in the list. You may assume all
numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return
[12, 9, 2, 1] since it sums up to 24.
"""


def subset_sum(arr, k):
    """Find a subset of number that add up to k."""
    arr.sort(reverse=True)
    while True:
        arr_sum = sum(arr)
        if arr_sum == k:
            break
        for i in arr:
            if (arr_sum - i) >= k:
                arr.remove(i)
                break
        else:
            return None
    return arr


print(subset_sum([12, 1, 61, 5, 9, 2], 24))    # [12, 9, 2, 1]
