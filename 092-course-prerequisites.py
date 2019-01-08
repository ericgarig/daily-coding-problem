"""
Daily Coding Problem - 2019-01-08.

We're given a hashmap associating each courseId key with a list of
courseIds values, which represents that the prerequisites of courseId
are courseIds. Return a sorted ordering of courses such that we can
finish all courses.

Return null if there is no such ordering.

For example, given {'CSC300': ['CSC100', 'CSC200'],
                    'CSC200': ['CSC100'],
                    'CSC100': []},
should return ['CSC100', 'CSC200', 'CSCS300'].
"""
import collections


def solve(d):
    """
    Given a list of prereqs, return the order courses must be taken in.

    NOTE: This assumes that courses are in only a single discipline
    ( and that courses prerequisites are a smaller course number ).
    """
    od = collections.OrderedDict(sorted(d.items()))
    result = []
    for id, prereq_list in od.items():
        for one_course in prereq_list:
            if one_course not in result:
                break
        else:
            result.append(id)
    return result


def solve_no_order_dict(d):
    """Return list of prereqs without using an ordered-dict."""
    result = []
    while True:
        for id, prereq_list in d.items():
            for one_course in prereq_list:
                if one_course not in result:
                    break
            else:
                result.append(id)
                del d[id]
                break
        else:
            if bool(d):
                return None
            return result



print(solve({'CSC300': ['CSC100', 'CSC200'],
             'CSC100': [],
             'CSC200': ['CSC100']
             }))    # ['CSC100', 'CSC200', 'CSCS300']


print(solve_no_order_dict({'CSC300': ['CSC100', 'CSC200'],
                           'CSC100': [],
                           'CSC200': ['CSC100']
                           }))    # ['CSC100', 'CSC200', 'CSCS300']
