"""
Daily Coding Problem - 2019-04-13.

You are given given a list of rectangles represented by min and max x- and
y-coordinates. Compute whether or not a pair of rectangles overlap each other.
If one rectangle completely covers another, it is considered overlapping.

For example, given the following rectangles:
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}

return True as the first and third rectangle overlap each other.
"""


def solve(arr):
    """Determine if a rectangle completely overlaps abother."""
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (
                arr[i]["top_left"][0] <= arr[j]["top_left"][0]
                and arr[i]["top_left"][1] <= arr[j]["top_left"][1]
                and (arr[j]["top_left"][0] + arr[j]["dimensions"][0])
                <= (arr[i]["top_left"][0] + arr[i]["dimensions"][0])
                and (arr[j]["top_left"][1] + arr[j]["dimensions"][1])
                <= (arr[i]["top_left"][1] + arr[i]["dimensions"][1])
            ):
                return True
    return False


assert (
    solve(
        [
            {"top_left": (1, 4), "dimensions": (3, 3)},
            {"top_left": (-1, 3), "dimensions": (2, 1)},
            {"top_left": (0, 5), "dimensions": (4, 3)},
        ]
    )
) is True
