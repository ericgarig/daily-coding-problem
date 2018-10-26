"""
Daily Coding Problem - 2018-10-25.

Given an array of integers and a number k, where 1 <= k <= length of the
array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get:
[10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. You can modify the input array
in-place and you do not need to store the results. You can simply print
them out as you compute them.
"""


def max_subarray(arr, k):
    """Get the max of each subarray of k items."""
    for cnt in xrange(k - 1):
        # loop over k - 1 times, each time taking the max of 2 adjacent values
        arr = [max(value, other) for value, other in zip(arr[:-1], arr[1:])]
    return arr


print(max_subarray([10, 5, 2, 7, 8, 7], 2))    # [10, 5, 7, 8, 8]
print(max_subarray([10, 5, 2, 7, 8, 7], 3))    # [10, 7, 8, 8]
print(max_subarray([10, 5, 2, 7, 8, 7], 4))    # [10, 8, 8]
print(max_subarray([10, 5, 2, 7, 8, 7], 5))    # [10, 8]


print(max_subarray([1, 2, 5, 3, 4, 4, 3, 2, 7], 3))    # [5, 5, 5, 4, 4, 4, 7]
