"""
Daily Coding Problem - 2019-03-23.

Implement a 2D iterator class. It will be initialized with an array of arrays,
and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more
elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next()
repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be
empty.
"""


class TwoDimIteror(object):
    """2D-array itetator."""

    def __init__(self, arr):
        """Init."""
        self.hit_ts = []
        self.arr = arr
        self.row = 0
        self.col = 0

    def has_next(self):
        """Determine whether or not the iterator still has elements left."""
        current_row = self.row
        current_col = self.col
        for i in self.arr[current_row:]:
            for j in i[current_col:]:
                if j:
                    return True
            current_col = 0
        return False

    def next(self):
        """Get the next element in the 2D array."""
        try:
            self.col += 1
            return self.arr[self.row][self.col - 1]
        except IndexError:
            self.col = 1
            self.row += 1
            try:
                while not self.arr[self.row]:
                    self.row += 1
                return self.arr[self.row][self.col - 1]
            except IndexError:
                return None


iter2D = TwoDimIteror([[1, 2], [3], [], [4, 5, 6]])
# 1
print(iter2D.has_next())
print(iter2D.next())
# 2
print(iter2D.has_next())
print(iter2D.next())
# 3
print(iter2D.has_next())
print(iter2D.next())
# 4
print(iter2D.has_next())
print(iter2D.next())
# 5
print(iter2D.has_next())
print(iter2D.next())
# 6
print(iter2D.has_next())
print(iter2D.next())
# done with array
print(iter2D.has_next())
print(iter2D.next())
