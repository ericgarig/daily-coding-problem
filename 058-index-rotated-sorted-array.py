"""
Daily Coding Problem - 2018-12-05.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in
faster than linear time. If the element doesn't exist in the array,
return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.
"""


def get_index(arr, k):
    """Return index of value in a rotated array."""
    index_l = 0
    index_r = len(arr) - 1
    while index_l <= index_r:
        index_m = index_l + ((index_r - index_l) // 2)
        if arr[index_m] == k:
            return index_m
        # left half is sorted
        if arr[index_l] <= arr[index_m]:
            if arr[index_l] <= k and k <= arr[index_m]:
                index_r = index_m - 1
            else:
                index_l = index_m + 1
        # right half is sorted
        else:
            if arr[index_m] <= k and k <= arr[index_r]:
                index_l = index_m + 1
            else:
                index_r = index_m - 1
    return None


print(get_index([13, 18, 25, 2, 8, 10], 8))    # 4
