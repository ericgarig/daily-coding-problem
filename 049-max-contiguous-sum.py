"""
Daily Coding Problem - 2018-11-25.

Given an array of numbers, find the maximum sum of any contiguous
subarray of the array.

For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum
would be 137, since we would take elements 42, 14, -5, and 86.

Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we
would not take any elements.

Do this in O(N) time.

"""


def solve(arr):
    """Return the max sum of contiguous sub-array."""
    total = 0
    totals_arr = [0]
    for i in arr:
        total += i
        totals_arr.append(total)

    max_peak = max(totals_arr)
    if max_peak == 0:
        return 0
    min_val = min(totals_arr[:totals_arr.index(max_peak)])
    return max_peak - min_val


print(solve([34, -50, 42, 14, -5, 86]))    # 137
print(solve([-5, -1, -8, -9]))    # 0
print(solve([10, 20, -32, 30]))    # 30
print(solve([10, 20, -29, 30]))    # 31
print(solve([10, 20, 30, -29]))    # 60
print(solve([-29, 10, 20, 30]))    # 60
print(solve([-10, -20, -29, 60]))    # 60
