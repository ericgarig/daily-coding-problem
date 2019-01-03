"""
Daily Coding Problem - 2018-10-28.

Given an array of time intervals (start, end) for classroom lectures
(possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


def min_classrooms(interval_list):
    """Given a list of time intervals, return min number of rooms."""
    interval_list.sort()
    room_end_times = [0]
    for start, end in interval_list:
        for room in range(len(room_end_times)):
            if room_end_times[room] <= start:
                room_end_times[room] = end
                break
        else:
            # unable to find a room, so we must add another
            room_end_times.append(end)
    return len(room_end_times)


print(min_classrooms([(30, 75), (0, 50), (60, 150)]))    # 2
