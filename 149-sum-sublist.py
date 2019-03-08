"""
Daily Coding Problem - 2019-03-07.

Given a list of numbers L, implement a method sum(i, j) which returns
the sum from the sublist L[i:j] (including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3) should return
sum([2, 3]), which is 5.

You can assume that you can do some pre-processing. sum() should be
optimized over the pre-processing step.

"""


class SubListSum:
    """Optimized sub list."""

    def __init__(self, arr):
        """Init."""
        self.arr = arr
        total = 0
        self.runningSum = [total]
        for i in arr:
            total += i
            self.runningSum.append(total)

    def sum(self, i, j):
        """Sum the sublist of arr from i (inc ) to j ( exc )."""
        if i < 0 or len(self.arr) < j or j <= i:
            return None
        return self.runningSum[j] - self.runningSum[i]


sls = SubListSum([1, 2, 3, 4, 5])
assert (sls.sum(1, 3)) == 5
assert (sls.sum(0, 1)) == 1
assert (sls.sum(0, 5)) == 15
assert (sls.sum(1, 1)) == None
assert (sls.sum(-1, 1)) == None
assert (sls.sum(2, 1)) == None
