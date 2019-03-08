"""
Daily Coding Problem - 2019-03-08.

Given a 2-D matrix representing an image, a location of a pixel in the
screen and a color C, replace the color of the given pixel and all
adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2),
and 'G' for green:

B B W
W W W
W W W
B B B
Becomes

B B G
G G G
G G G
B B B
"""


def solve(arr, pos, color):
    """Given a 2D array, position, and color, change all adjacent colors."""
    i = 0
    same_color = [pos]
    while i < len(same_color):
        for j in get_neighbors(arr, same_color[i], arr[pos[0]][pos[1]]):
            if j not in same_color:
                same_color.append(j)
        i += 1
    for i in same_color:
        arr[i[0]][i[1]] = color
    return arr


def get_neighbors(arr, pos, color):
    """Return neighbors with the same color."""
    neighbors = []
    try:
        if arr[pos[0] + 1][pos[1]] == color:
            neighbors.append((pos[0] + 1, pos[1]))
    except IndexError:
        pass
    try:
        if arr[pos[0] - 1][pos[1]] == color:
            neighbors.append((pos[0] - 1, pos[1]))
    except IndexError:
        pass
    try:
        if arr[pos[0] + 1][pos[1]] == color:
            neighbors.append((pos[0] + 1, pos[1]))
    except IndexError:
        pass
    try:
        if arr[pos[0]][pos[1] - 1] == color:
            neighbors.append((pos[0], pos[1] - 1))
    except IndexError:
        pass
    return neighbors


input_matrix = [
    ["B", "B", "W"],
    ["W", "W", "W"],
    ["W", "W", "W"],
    ["B", "B", "B"],
]
output_matrx = [
    ["B", "B", "G"],
    ["G", "G", "G"],
    ["G", "G", "G"],
    ["B", "B", "B"],
]
assert (solve(input_matrix, (2, 2), "G")) == output_matrx
