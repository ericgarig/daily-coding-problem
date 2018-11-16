"""
Daily Coding Problem - 2018-11-16.

Given an array of integers where every integer occurs three times except
for one integer, which only occurs once, find and return the
non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1.
Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
"""


def unique_int(arr):
    """
    Given an array, return unique integer.

    Difference of 3x of sum of the set of the array and sum of the array
    is twice the difference of the integer that appears only once.
    """
    return (sum(set(arr)) * 3 - sum(arr)) // 2


print(unique_int([6, 1, 3, 3, 3, 6, 6]))    # 1
print(unique_int([13, 19, 13, 13]))    # 19
