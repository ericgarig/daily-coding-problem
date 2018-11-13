"""
Daily Coding Problem - 2018-11-13.

The power set of a set is the set of all its subsets. Write a function
that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""


def power_set(arr=None, parent_arr=None):
    """Return the power set of a set."""
    if not arr:
        return []
    if parent_arr is None:
        parent_arr = []
    result = []
    for i in range(len(arr)):
        one_e = arr[i]
        one_list = list(parent_arr)
        one_list.append(one_e)
        result.append(one_list)
        result.extend(power_set(arr[(i + 1):], one_list))
    if parent_arr == []:
        # top-level call, so add the empty set to the power set.
        result.append([])
    return result


print(power_set([7, 8, 9]))
# [[], [7], [8], [9], [7, 8], [7, 9], [8, 9], [7, 8, 9]]
