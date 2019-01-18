u"""
Daily Coding Problem - 2018-12-31.

Given a mapping of digits to letters (as in a phone number), and a digit
string, return all possible letters the number could represent. You can
assume each valid number in the mapping is a single digit.

For example if {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], …} then '23'
should return ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].
"""


def solve(d={}, code_str='', mapping=[]):
    """Return string mapping."""
    if len(code_str) == 0:
        return mapping
    first_str = code_str[:1]
    if mapping == []:
        new_map = d[first_str]
    else:
        new_map = []
        for i in mapping:
            for j in d[first_str]:
                new_map.append(''.join([i, j]))
    return solve(d, code_str[1:], new_map)


# ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
result = solve({'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f']}, '23')
print(result)
