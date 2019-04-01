"""
Daily Coding Problem - 2019-03-28.

You are given a list of data entries that represent entries and exits of groups
of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most
people in the building. Return it as a pair of (start, end) timestamps.
You can assume the building always starts off and ends up empty,
i.e. with 0 people inside.
"""


def solve(arr):
    """Find the busiest time."""
    max_count = 0
    cur_count = 0
    timeframe = ()
    for i in range(len(arr)):
        if arr[i]["type"] == "enter":
            cur_count += arr[i]["count"]
        else:
            cur_count -= arr[i]["count"]
        if cur_count >= max_count:
            max_count = cur_count
            try:
                timeframe = (arr[i]["timestamp"], arr[i + 1]["timestamp"])
            except IndexError:
                return (arr[i]["timestamp"], None)
    return timeframe


entry_log = [
    {"timestamp": 1526579928, "count": 3, "type": "enter"},
    {"timestamp": 1526580382, "count": 2, "type": "exit"},
    {"timestamp": 1526580482, "count": 4, "type": "enter"},
    {"timestamp": 1526580500, "count": 2, "type": "exit"},
    {"timestamp": 1526581000, "count": 1, "type": "enter"},
]
assert (solve(entry_log)) == (1526580482, 1526580500)

entry_log.append({"timestamp": 1526582000, "count": 10, "type": "enter"})
assert (solve(entry_log)) == (1526582000, None)
