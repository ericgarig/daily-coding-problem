"""
Daily Coding Problem - 2019-01-22.

Given an integer list where each number represents the number of hops you can
make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false.
"""


def solve(arr=[]):
    """
    Determine if we can jump through the array to get to the end.

    NOTE: keep track of the visited indexes so we're not in an infinite loop.
    """
    i = 0
    visited_index_list = []
    while True:
        if i == len(arr) - 1:
            return True
        if arr[i] == 0:
            return False
        visited_index_list.append(i)
        i += arr[i]
        if i in visited_index_list:
            return False


assert (solve([2, 0, 1, 0])) == True
assert (solve([1, 1, 0, 1])) == False
assert (solve([1, 2, 3, 1, -2, 0])) == True
assert (solve([1, -1, 0])) == False
