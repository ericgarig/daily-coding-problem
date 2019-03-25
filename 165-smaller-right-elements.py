"""
Daily Coding Problem - 2019-03-21.

Given an array of integers, return a new array where each element in the
new array is the number of smaller elements to the right of that element
in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:

There is 1 smaller element to the right of 3
There is 1 smaller element to the right of 4
There are 2 smaller elements to the right of 9
There is 1 smaller element to the right of 6
There are no smaller elements to the right of 1
"""


def solve_from_end(arr):
    """Get an array of smaller elements to the right of the original array."""
    smaller_arr = [0]
    arr_index = len(arr) - 2
    while arr_index >= 0:
        smaller_count = 0
        for j in arr[arr_index:]:
            if arr[arr_index] > j:
                smaller_count += 1
        smaller_arr.append(smaller_count)
        arr_index -= 1
    smaller_arr.reverse()
    return smaller_arr


def solve_from_beginning(arr):
    """Same as above, but step go L->R instead of going in reverse."""
    smaller_arr = []
    for i in range(len(arr)):
        smaller_count = 0
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                smaller_count += 1
        smaller_arr.append(smaller_count)
    return smaller_arr


assert (solve_from_end([3, 4, 9, 6, 1])) == [1, 1, 2, 1, 0]
assert (solve_from_beginning([3, 4, 9, 6, 1])) == [1, 1, 2, 1, 0]
