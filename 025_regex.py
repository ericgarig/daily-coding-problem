"""
Daily Coding Problem - 2018-11-01.

Implement regular expression matching with the following special characters:
. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element

That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular
expression.

E.g.:
Given the regular expression "ra." and the string "ray", your function
should return true. The same regular expression on the string "raymond"
should return false.

Given the regular expression ".*at" and the string "chat", your function
should return true. The same regular expression on the string "chats"
should return false.
"""


def regex(test_str, pattern):
    """Given a string and a pattern, return if the str matches the pattern."""
    while test_str or pattern:
        if not test_str or not pattern:
            return False
        pattern_char = pattern[0]
        if pattern_char == '.':
            test_str = test_str[1:]
            pattern = pattern[1:]
        elif pattern_char == '*':
            if len(pattern) == 1:
                return True
            else:
                for i in pattern[1:]:
                    if i != '*':
                        if i == '.':
                            test_str = test_str[1:]
                            pattern = pattern[2:]
                        else:
                            str_pos = test_str.find(i)
                            if str_pos == -1:
                                return False
                            test_str = test_str[str_pos + 1:]
                            pattern = pattern[2:]
                        break
        elif pattern_char == test_str[0]:
            test_str = test_str[1:]
            pattern = pattern[1:]
        else:
            return False
    return True


print(regex('ray', 'ra.'))
print(regex('raymond', 'ra.'))
print(regex('chat', '.*at'))
print(regex('chats', '.*at'))
print(regex('chats', '*.*'))
print(regex('chats', '*'))
