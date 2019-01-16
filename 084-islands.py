"""
Daily Coding Problem - 2018-12-31.

Given a matrix of 1s and 0s, return the number of "islands" in the
matrix. A 1 represents land and 0 represents water, so an island is a
group of 1s that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
"""


def solve(arr):
    """Find the number of islands."""
    islands = {}
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            if arr[row][col]:
                islands[tuple([row, col])] = add_neighbors(arr, row, col)
    islands = combine_points(islands)
    return len(islands)


def add_neighbors(arr, x, y):
    """Given a point in a 2D array, add neighbors."""
    result = []
    max_x = len(arr)
    max_y = len(arr[x])
    if (y + 1) < max_y and arr[x][y + 1]:
        result.append([x, y + 1])
    if (y - 1) >= 0 and arr[x][y - 1]:
        result.append([x, y - 1])
    if (x + 1) < max_x and arr[x + 1][y]:
        result.append([x + 1, y])
    if (x - 1) >= 0 and arr[x - 1][y]:
        result.append([x - 1, y])
    return result


def combine_points(d):
    """Combine points of islands."""
    for key in list(d):
        try:
            neighbors = d[key]
            for point in neighbors:
                possible_key = tuple(point)
                if d[possible_key] and possible_key != key:
                    neighbors = d[key]
                    [neighbors.append(i)
                     for i in d[possible_key]
                     if i not in neighbors and i != list(key)]
                    d[key] = neighbors
                    del d[possible_key]
        except KeyError:
            # key deleted ( and neighbors merged ) because it's a neighbor
            pass
    return d


arr = [[1, 0, 0, 0, 0],
       [0, 0, 1, 1, 0],
       [0, 1, 1, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 0, 1],
       [1, 1, 0, 0, 1]]
print(solve(arr))    # 4
