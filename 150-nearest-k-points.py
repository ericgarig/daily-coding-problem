"""
Daily Coding Problem - 2019-03-07.

Given a list of points, a central point, and an integer k, find the
nearest k points from the central point.

For example, given the list of points [(0, 0), (5, 4), (3, 1)], the
central point (1, 2), and k = 2, return [(0, 0), (3, 1)].
"""


def solve(arr, pos, k=0):
    """Given a 2D array, position, return the closest k points."""
    if k > len(arr):
        return None
    distance = [abs(i[0] - pos[0]) + abs(i[1] - pos[1]) for i in arr]
    max_distance = max(distance)
    result = []
    for i in range(k):
        min_index = distance.index(min(distance))
        result.append(arr[min_index])
        distance[min_index] = max_distance + 1
    return result


assert (solve([(0, 0), (5, 4), (3, 1)], (1, 2), 2)) == [(0, 0), (3, 1)]
