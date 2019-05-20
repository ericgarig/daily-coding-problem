"""
Daily Coding Problem - 2019-05-02.

A permutation can be specified by an array P, where P[i] represents the
location of the element at i in the permutation. For example, [2, 1, 0]
represents the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For
example, given the array ["a", "b", "c"] and the permutation [2, 1, 0],
return ["c", "b", "a"].
"""


def solve(arr, per):
    """Apply permutation to array."""
    for i in range(len(per)):
        if i != per[i]:
            swap_i = per[i]
            arr[i], arr[swap_i] = arr[swap_i], arr[i]
            per[i], per[swap_i] = per[swap_i], per[i]
    return arr


assert (solve(["a", "b", "c"], [2, 1, 0])) == ["c", "b", "a"]
assert (solve([1, 2, 3, 6, 7, 8], [0, 4, 2, 1, 3, 5])) == [1, 6, 3, 7, 2, 8]
