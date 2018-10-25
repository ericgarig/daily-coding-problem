"""
Daily Coding Problem - 2018-10-09.

Given an array of integers, return a new array such that each element at
index iof the new array is the product of all the numbers in the original
array except the one at i.

E.g.: given [1, 2, 3, 4, 5], the result should be [120, 60, 40, 30, 24]
      given [3, 2, 1], the result should be  [2, 3, 6].

Bonus: what if you can't use division?
"""


import numpy as np


def list_product_no_index(the_list):
    """
    Base solution.

    Get the product once via numpy and create a new list via list comprehension
    O(n)
    """
    total = np.prod(the_list)
    return [total / i for i in the_list]


def list_product_bonus(the_list):
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


list_product_no_index([1, 2, 3, 4, 5])
list_product_no_index([3, 2, 1])

list_product_bonus([1, 2, 3, 4, 5])
list_product_bonus([3, 2, 1])
