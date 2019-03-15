"""
Daily Coding Problem - 2018-10-09.

Given an array of integers, return a new array such that each element at
index i of the new array is the product of all the numbers in the
original array except the one at i.

E.g.: given [1, 2, 3, 4, 5], the result should be [120, 60, 40, 30, 24]
      given [3, 2, 1], the result should be  [2, 3, 6].

Bonus: what if you can't use division?
"""


import numpy as np


def solve_numpy(the_list):
    """
    Base solution.

    Get the product once via numpy and create a new list via list comprehension
    O(n)
    """
    total = np.prod(the_list)
    return [total / i for i in the_list]


def solve_no_division(the_list):
    """
    Extra solution is to do with without division.

    This is not the cleanest way to do this as we need to loop once per item.
    O(n**2)
    """
    new_list = []
    for i, v in enumerate(the_list):
        the_list[i] = 1
        new_list.append(np.prod(the_list))
        the_list[i] = v
    return new_list


def solve_standard_no_div(arr):
    """No division using only the standard library."""
    total = 1
    total_left = [total]
    for i in arr:
        total *= i
        total_left.append(total)
    total = 1
    total_right = [total]
    for i in arr[::-1]:
        total *= i
        total_right.append(total)
    total_right.reverse()
    result = []
    for i in range(len(arr)):
        result.append(total_left[i] * total_right[i + 1])
    return result


assert (solve_numpy([1, 2, 3, 4, 5])) == [120, 60, 40, 30, 24]
assert (solve_numpy([3, 2, 1])) == [2, 3, 6]

assert (solve_no_division([1, 2, 3, 4, 5])) == [120, 60, 40, 30, 24]
assert (solve_no_division([3, 2, 1])) == [2, 3, 6]

assert (solve_standard_no_div([1, 2, 3, 4, 5])) == [120, 60, 40, 30, 24]
assert (solve_standard_no_div([3, 2, 1])) == [2, 3, 6]
