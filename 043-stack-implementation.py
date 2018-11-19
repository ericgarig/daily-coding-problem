"""
Daily Coding Problem - 2018-11-19.

Implement a stack that has the following methods:
 - push(val), which pushes an element onto the stack
 - pop(), which pops off and returns the topmost element of the stack.
    If there are no elements in the stack, then it should throw an error
    or return null.
 - max(), which returns the maximum value in the stack currently.
    If there are no elements in the stack, then it should throw an error
    or return null.

Each method should run in constant time.
"""


class NewStack(object):
    """Implement a stack data structure."""

    def __init__(self):
        """Init."""
        self.val_list = []
        self.max_list = []

    def __repr__(self):
        """Display a user-friendly represenation of the stack."""
        return str(self.val_list)

    def push(self, val):
        """Push a new value on the stack."""
        self.val_list.append(val)
        self.max_list.append(max(val, self.max()) if self.max_list else val)

    def pop(self):
        """Remove the last value from the stack."""
        self.max_list.pop()
        return self.val_list.pop()

    def max(self):
        """Return the maximum value."""
        return self.max_list[-1]


max_stack = NewStack()
max_stack.push(1)
max_stack.push(2)
max_stack.push(1)
max_stack.push(4)
max_stack.push(2)
max_stack.push(3)
print(max_stack)
print(max_stack.max())
max_stack.pop()
max_stack.pop()
max_stack.pop()
print(max_stack)
print(max_stack.max())
