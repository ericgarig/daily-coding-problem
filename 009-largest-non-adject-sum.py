"""
Daily Coding Problem - 2018-10-16.

Given a list of integers, write a function that returns the largest sum
of non-adjacent numbers. Numbers can be 0 or negative.

E.g.: [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5
      [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""


def non_adjecent_sum(the_list):
    """Return largest non-adject sum of intergers in a list."""
    incl, excl = 0, 0
    for i in the_list:
        new_excl = max(excl, incl)

        # incl is sum of excl and this since adjacent values cannot be used
        incl = excl + i
        excl = new_excl
    return max(incl, excl)


non_adjecent_sum([3, 5, 7, 6])    # 11
non_adjecent_sum([1, 4, 3, 5, 2])    # 9
non_adjecent_sum([2, 4, 6, 2, 5])    # 13
non_adjecent_sum([5, 1, 1, 5])    # 10
non_adjecent_sum([-5, 1, 1, 5])    # 6
non_adjecent_sum([-5, 1, 1, -5])    # 1
