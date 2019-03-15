"""
Daily Coding Problem - 2019-02-17.

Design and implement a HitCounter class that keeps track of requests (or hits).
It should support the following operations:

 - record(timestamp): records a hit that happened at timestamp
 - total(): returns the total number of hits recorded
 - range(lower, upper): returns the number of hits that occurred between
 timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
"""


"""
Follow-up answer:

If system has limited memory, write list to a file when the length is
above a certain number ( say 1000, 5000, 10000, etc... ) and store reference
to that file as part of the class.
 - total() would instead return the sum of (# of items in the current list )
 and (# files * max length of list)
 - range() would loop over each file and append to the counter of hits
 registered within the bounds ( can exit once hits are outside of the
 upper bound).
"""


class HitCounter(object):
    """Hit Counter class."""

    def __init__(self):
        """Init."""
        self.hit_ts = []

    def record(self, timestamp):
        """Record a hit at a timestamp."""
        self.hit_ts.append(timestamp)
        return True

    def total(self):
        """Return the total number of hits recorded."""
        return len(self.hit_ts)

    def range(self, lower, upper):
        """Number of hits that occurred between timestamps (inclusive)."""
        if upper < lower:
            lower, upper = upper, lower
        return len([i for i in self.hit_ts if lower <= i and i <= upper])


hc = HitCounter()
hc.record(2)
hc.record(4)
hc.record(6)
hc.record(8)

assert (hc.range(3, 7)) == 2
assert (hc.range(7, 7)) == 0
assert (hc.range(7, 2)) == 3
