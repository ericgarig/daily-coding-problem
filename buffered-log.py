"""
Daily Coding Problem - 2018-10-23.

You run an e-commerce website and want to record the last N order ids in
a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log.
             i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""
from collections import deque


class OrderLog(object):
    """Order Log class that keeps track of N number of orders ( items )."""

    def __init__(self, items):
        """Init."""
        self.items = items
        self.q = deque([], maxlen=items)

    def __repr__(self):
        """Representation."""
        return 'OrderLog %s' % self.q

    def record(self, order_id):
        """Add new item to log."""
        return self.q.append(order_id)

    def get_last(self, i):
        """View the most recent i orders."""
        return list(self.q)[-i:]


log = OrderLog(10)
for i in range(10, 20):
    log.record(i)
print(log)

print('last 3 elements: %s' % log.get_last(3))

print('adding order 20')
log.record(20)
print('adding order 30')
log.record(30)

print('last 3 elements: %s' % log.get_last(3))

print(log)
