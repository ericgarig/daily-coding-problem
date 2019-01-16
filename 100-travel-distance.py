"""
Daily Coding Problem - 2019-01-16.

You are in an infinite 2D grid where you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to
cover the points. Give the minimum number of steps in which you can
achieve it. You start from the first point.

Example:
    Input: [(0, 0), (1, 1), (1, 2)]
    Output: 2

    It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to
    move from (1, 1) to (1, 2).
"""


def solve(arr):
    """Find the number of steps to hit every point."""
    result = 0
    prev_point = arr[0]
    for point in arr:
        result += travel_distance(prev_point, point)
        prev_point = point
    return result


def travel_distance(point_a, point_b):
    """
    Determine the distance between 2 points.

    We need to take the maximum of the difference of the x and y coordinates
    since we can move in all 8 directions. If we were limited to
    up/down/left/right, we would need to get the total instead.
    """
    return max(abs(point_a[0] - point_b[0]), abs(point_a[1] - point_b[1]))


print(solve([(0, 0), (1, 1), (1, 2)]))    # 2
print(solve([(0, 0), (2, 0), (2, 2)]))    # 4
