"""
Daily Coding Problem - 2019-04-23.

Given an array and a number k that's smaller than the length of the array,
rotate the array to the right k elements in-place.
"""


def solve(arr, k):
    """Given an array, rotate in by k elements."""
    if k < 1:
        return arr
    first_element = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[-1] = first_element
    return solve(arr, k - 1)


assert (solve([1, 2, 3, 4, 5, 6], 2)) == [3, 4, 5, 6, 1, 2]
assert (solve([1, 2, 3, 4, 5, 6], 1)) == [2, 3, 4, 5, 6, 1]
assert (solve([1, 2, 3, 4, 5, 6], 6)) == [1, 2, 3, 4, 5, 6]
assert (solve([1, 2, 3, 4, 5, 6], 7)) == [2, 3, 4, 5, 6, 1]
