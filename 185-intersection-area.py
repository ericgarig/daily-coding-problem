"""
Daily Coding Problem - 2019-04-11.

Given two rectangles on a 2D graph, return the area of their intersection.
If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
"""


def solve(r1, r2):
    """Given 2 rectangles, return the instersecting area."""
    intersect_left = max(r1["top_left"][0], r2["top_left"][0])
    intersect_top = max(r1["top_left"][1], r2["top_left"][1])
    intersect_right = min(
        r1["top_left"][0] + r1["dimensions"][0],
        r2["top_left"][0] + r2["dimensions"][0],
    )
    intersect_bottom = min(
        r1["top_left"][1] + r1["dimensions"][1],
        r2["top_left"][1] + r2["dimensions"][1],
    )
    return (intersect_bottom - intersect_top) * (
        intersect_right - intersect_left
    )


assert (
    solve(
        {"top_left": (1, 4), "dimensions": (3, 3)},  # width, height
        {"top_left": (0, 5), "dimensions": (4, 3)},  # width, height
    )
) == 6
