"""
Daily Coding Problem - 2018-10-11.

Given an array of integers, find the first missing positive integer in
linear time and constant space. In other words, find the lowest positive
integer that does not exist in the array. The array can contain duplicates
and negative numbers as well.

E.g.: given [3, 4, -1, 1], the result should be 2
      given [1, 2, 0], the result should be  3.

You can modify the input array in-place.
"""


def first_missing_num(the_list):
    """
    Sorted solution.

    Due to sort, the time complexity is O(nlogn).
    This solution is done in constant space.
    """
    the_list.sort()
    first_index = 0
    next_min = 0
    for i, v in enumerate(the_list):
        if v > 0:
            first_index = i
            next_min = v
            break
    for num in the_list[first_index:]:
        if num < next_min:
            continue
        elif num == next_min:
            next_min += 1
        else:
            return next_min
    return next_min


assert (first_missing_num([3, 4, -1, 1])) == 2
assert (first_missing_num([1, 2, 5, 2, 3])) == 4
assert (first_missing_num([1, 2, 3])) == 4
assert (first_missing_num([4, 7, 3, 5, 5, 3, 7])) == 6
