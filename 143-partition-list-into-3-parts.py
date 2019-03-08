"""
Daily Coding Problem - 2019-02-28.

Given a pivot x, and a list lst, partition the list into three parts.

The first part contains all elements in lst that are less than x
The second part contains all elements in lst that are equal to x
The third part contains all elements in lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], one
partition may be [9, 3, 5, 10, 10, 12, 14].
"""


def solve(arr=[], x=None):
    """Partition list into 3 parts."""
    p1 = []
    p2 = []
    p3 = []
    for i in arr:
        if i < x:
            p1.append(i)
        elif i == x:
            p2.append(i)
        else:
            p3.append(i)
    p1.extend(p2)
    p1.extend(p3)
    return p1


def solve_in_place(arr=[], x=None):
    """Partition the list into 3 parts, but do this IN PLACE."""
    # swap so that all values less than x are first
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] >= x:
            arr[start], arr[end] = arr[end], arr[start]
        if arr[start] < x:
            start += 1
        if arr[end] < x:
            arr[start + 1], arr[end] = arr[end], arr[start + 1]
        if arr[end] >= x:
            end -= 1

    # find first index of the pivot
    pivot_index = 0
    for i, v in enumerate(arr):
        if v >= x:
            pivot_index = i
            break

    # swap so that all instances of x are first
    end = len(arr) - 1
    while pivot_index < end:
        if arr[pivot_index] == x:
            pivot_index += 1
        if arr[end] == x:
            arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
            pivot_index += 1
            end -= 1
    return arr


assert (solve([9, 12, 3, 5, 14, 10, 10], 10)) == [9, 3, 5, 10, 10, 12, 14]
assert (solve_in_place([9, 12, 3, 5, 14, 10, 10], 10)) == [
    9,
    5,
    3,
    10,
    10,
    12,
    14,
]
