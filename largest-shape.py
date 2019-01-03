"""
Coding Problem.

Given a 2-dimentional array such that each item represents a pixel that is
either on or off, return the size of the biggest conginuous shape and a
pixel inside the shape.

A shape is considered contiguous if for a given pixel that is on, a the
neighbor ( left/right/above/below, not diagonally ) is also on.

For example, given a matrix such as:

...........xxx.
.xxx..xxx....x.
.xxx..x.x..xxx.
.xxx..xxx....x.
...........xxx.

where (x) represent on and (.) represents off, the return 11 and a [0, 11]
"""


def largest_shape(arr):
    """Given a 2 dimentional array, find the size of the biggest shape."""
    on_pixels = get_on_pixels(arr)
    pixel_dict = get_pixel_dict(on_pixels)
    grouped_dict = combine_shapes(pixel_dict)
    return get_biggest_shape(grouped_dict)


def get_biggest_shape(dict):
    """Given a dict of neighboring pixels, find the biggest shape."""
    max_key = ''
    max_size = 0
    for key in dict.keys():
        if len(dict[key]) > max_size:
            max_key = list(key)
            max_size = len(dict[key]) + 1
    return max_key, max_size


def combine_shapes(dict):
    """Group neighbors."""
    for key in dict.keys():
        i = 0
        while i < len(dict[key]):
            # loop over each neighboring pixel and append its neighbors
            neighbor_key = tuple(dict[key][i])
            if neighbor_key in dict:
                neighbors = add_missing_neighbors(dict[key],
                                                  dict[neighbor_key],
                                                  list(key))
                dict[key] = neighbors
                dict[neighbor_key] = []
            i += 1
    return dict


def add_missing_neighbors(list_a, list_b, self_coord):
    """Append items from list_b that aren't in list_a, and preserve order."""
    for i in list_b:
        if i not in list_a and i != self_coord:
            list_a.append(i)
    return list_a


def get_on_pixels(arr):
    """Given a shape, return all the pixels that are on."""
    pixels = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if shape[i][j]:
                pixels.append([i, j])
    return pixels


def get_pixel_dict(arr):
    """Get a dictionary of neighboring on pixel in the array."""
    pixel_dict = {}
    for i in arr:
        key = tuple(i)
        pixel_dict[key] = get_neighbors(arr, i)
    return pixel_dict


def get_neighbors(arr, pixel):
    """Get a list of neighboring on pixels."""
    on_neighbors = []
    x = pixel[0]
    y = pixel[1]
    if [x, y + 1] in arr:
        on_neighbors.append([x, y + 1])
    if [x, y - 1] in arr:
        on_neighbors.append([x, y - 1])
    if [x + 1, y] in arr:
        on_neighbors.append([x + 1, y])
    if [x - 1, y] in arr:
        on_neighbors.append([x - 1, y])
    return on_neighbors


shape = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
         [0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
         [0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0]]
print(largest_shape(shape))
