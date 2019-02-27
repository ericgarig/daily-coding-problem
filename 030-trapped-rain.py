"""
Daily Coding Problem - 2018-11-06.

You are given an array of non-negative integers that represents a
two-dimensional elevation map where each element is unit-width wall and
the integer is the height. Suppose it will rain and all spots between
two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time
and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in
the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first
index, 2 in the second, and 3 in the fourth index (we cannot hold 5
since it would run off to the left), so we can trap 8 units of water.
"""


def measure_rain(arr):
    """
    Given an array, measure the amount of water that can be collected.

    This assumes the right wall is higher than the left wall.
    """
    potential_water = []
    start_height = 0
    stored_water = 0
    for i in arr:
        if i >= start_height:
            for j in potential_water:
                stored_water += j
            start_height = i
            potential_water = []
        else:
            potential_water.append(start_height - i)
    return stored_water


print(measure_rain([3, 0, 1, 3, 0, 5]))  # 8
