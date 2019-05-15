"""
Daily Coding Problem - 2019-04-29.

Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand. Find the minimum element in O(log N) time. You may assume the
array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
"""


def solve(arr):
    """Get the index of min element in a pivoted sorted array."""
    start = 0
    end = len(arr) - 1
    pivot = (end + start) // 2
    while True:
        if arr[start] < arr[end]:
            # first element
            return start
        if pivot == end and arr[pivot] < arr[pivot - 1]:
            # last element
            return pivot
        elif arr[pivot] < arr[pivot + 1] and arr[pivot] < arr[pivot - 1]:
            # pivot is min
            return pivot
        elif arr[end] < arr[pivot]:
            # min to the right of pivot
            start = pivot
            pivot = (end + start) // 2
            if start == pivot:
                pivot += 1
        else:
            # min to the left of pivot
            end = pivot
            pivot = (end + start) // 2


assert (solve([5, 7, 10, 3, 4])) == 3
assert (solve([7, 10, 3, 4, 5])) == 2
assert (solve([3, 4, 5, 7, 10])) == 0
assert (solve([4, 5, 7, 10, 3])) == 4
