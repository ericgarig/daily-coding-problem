"""
Daily Coding Problem - 2018-10-12.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the
first and last element of that pair. Implement car and cdr.

E.g.: car(cons(3, 4)) returns 3
      cdr(cons(3, 4)) returns 4
"""


def cons(a, b):
    """Construct a pair."""
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    """Return the FIRST element of the pair."""
    return pair(lambda a, b: a)


def cdr(pair):
    """Return the LAST element of the pair."""
    return pair(lambda a, b: b)


car(cons(3, 4))    # returns 3
cdr(cons(3, 4))    # returns 4
cdr(car(cons(cons(3, 4), cons(1, 2))))    # returns 4
cdr(cdr(cons(cons(3, 4), cons(1, 2))))    # returns 2
car(cdr(cons(cons(3, 4), cons(1, 2))))    # returns 1
