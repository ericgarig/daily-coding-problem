"""
Daily Coding Problem - 2019-01-11.

Given a number represented by a list of digits, find the next greater
permutation of a number, in terms of lexicographic ordering. If there is
not greater permutation possible, return the permutation with the lowest
value/ordering.

For example, the list [1,2,3] should return [1,3,2]. The list [1,3,2]
should return [2,1,3]. The list [3,2,1] should return [1,2,3].

Can you perform the operation without allocating extra memory
(disregarding the input memory)?
"""


def solve(arr):
    """Find the next biggest permutation, or the smallest if not possible."""
    if sorted(arr, reverse=True) == arr:
        arr.sort()
        return arr
    # find the first decreasing element
    # swap with the next largest element
    # sort right part of the array ( after swapped next largest element)
    pass


print(solve([1, 2, 3]))    # [1, 3, 2]
print(solve([1, 3, 2]))    # [2, 1, 3]
print(solve([3, 2, 1]))    # [1, 2, 3]
