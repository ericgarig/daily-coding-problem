"""
Daily Coding Problem - 2018-11-17.

Given an unordered list of flights taken by someone, each represented as
(origin, destination) pairs, and a starting airport, compute the
person's itinerary. If no such itinerary exists, return null. If there
are multiple possible itineraries, return the lexicographically smallest
one. All flights must be used in the itinerary.

For example, given the list of flights
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and
starting airport 'YUL', you should return the list
['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting
airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
and starting airport 'A', you should return the list
['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also
a valid itinerary. However, the first one is lexicographically smaller.



SELF NOTE:
This solution does not cover the case where you have to recursively back
up if you encounter an invalid itenirary so you could try another option.
For example, given the list of flights [('A', 'B'), ('A', 'C'), ('C', 'A')]
and starting in 'A', the algorithm would pick 'A' --> 'B', then error.
If we implement backing out, the correct result is ['A', 'C', 'A', 'B'].
"""


def flight_tracker(flights=None, start_city=None):
    """Print out the visited cities."""
    if flights is None or start_city is None:
        return None
    stops = [start_city]
    while flights:
        possible_routes = [route for route in flights if route[0] == stops[-1]]
        if not possible_routes:
            return None
        possible_routes.sort()
        chosen_flight = possible_routes[0]
        stops.append(chosen_flight[1])
        flights.remove(chosen_flight)
    return stops


# ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
print(flight_tracker([('SFO', 'HKO'),
                      ('YYZ', 'SFO'),
                      ('YUL', 'YYZ'),
                      ('HKO', 'ORD')], 'YUL'))

print(flight_tracker([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))    # null
print(flight_tracker([('A', 'B'),
                      ('A', 'C'),
                      ('B', 'C'),
                      ('C', 'A')], 'A'))    # ['A', 'B', 'C', 'A', 'C'
