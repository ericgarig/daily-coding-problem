"""
Daily Coding Problem - 2019-02-06.

Given a string which we can delete at most k, return whether you can
make a palindrome.

For example, given 'waterrfetawx' and a k of 2, you could delete f and x
to get 'waterretaw'.
"""


def solve(some_str="", k=0):
    """Determine if a palindrome is exists with at most k-chars are removed."""
    start = 0
    end = len(some_str)
    skip_char_list = []
    while start < end:
        if len(skip_char_list) > k:
            return None
        # if not the same:
        # iterate from back uptil hitting start. if removed under k, return
        # iterate from start to end. if removed under k, return
        # remove start and end if remove above k both both above

        # add skipped index to list
        start += 1
        end -= 1

    # iterate over some_str, removing indexes from list, return
    return some_str


print(solve("waterrfetawx", 2))  # waterretaw
