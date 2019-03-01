"""
Daily Coding Problem - 2019-03-01.

Given an array of numbers and an index i, return the index of the nearest
larger number of the number at index i, where distance is measured in
array indices.

For example, given [4, 1, 3, 5, 6] and index 0, you should return 3.

If two distances to larger numbers are the equal, then return any one of
them. If the array at i doesn't have a nearest larger integer, then
return null.

Follow-up: If you can preprocess the array, can you do this in constant time?
"""


def solve(arr=[], k=None):
    """Return index of closest larger number in the array."""
    d = [abs(i - k) if arr[i] > arr[k] else len(arr) for i in range(len(arr))]
    min_index = d.index(min(d))
    if d[min_index] == len(arr):
        return None
    return min_index


print(solve([4, 1, 3, 5, 6], 0))  # 3
print(solve([4, 1, 3, 5, 6], 2))  # 3
print(solve([4, 1, 3, 2, 6], 2))  # 0
print(solve([4, 1, 3, 2, 6], 4))  # None
