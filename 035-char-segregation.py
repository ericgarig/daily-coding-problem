"""
Daily Coding Problem - 2018-11-11.

Given an array of strictly the characters 'R', 'G', and 'B', segregate
the values of the array so that all the Rs come first, the Gs come
second, and the Bs come last. You can only swap elements of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it
should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].
"""


def char_sep(arr=None):
    """Segreate the specified array in the order of R, G, B."""
    if not arr:
        return None
    left_i = 0
    right_i = len(arr) - 1
    # move Rs to the front
    while True:
        # find first non-R
        while arr[left_i] == 'R' and left_i < right_i:
            left_i += 1

        # find last R
        while arr[right_i] != 'R' and left_i < right_i:
            right_i -= 1

        # indexes reached each other, so there are no more
        if left_i >= right_i:
            break

        # swap
        arr[left_i], arr[right_i] = arr[right_i], arr[left_i]

    left_i = 0
    right_i = len(arr) - 1
    # move Bs to the end
    while True:
        # find first B
        while arr[left_i] != 'B' and left_i < right_i:
            left_i += 1

        # find last B
        while arr[right_i] == 'B' and left_i < right_i:
            right_i -= 1

        # indexes reached each other, so there are no more
        if left_i >= right_i:
            break

        # swap
        arr[left_i], arr[right_i] = arr[right_i], arr[left_i]\

    return arr


print(char_sep(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
# ['R', 'R', 'R', 'G', 'G', 'B', 'B']
