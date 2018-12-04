"""
Daily Coding Problem - 2018-12-04.

Given a string s and an integer k, break up the string into multiple
texts such that each text has a length of k or less. You must break it
up so that words don't break across lines. If there's no way to break
the text up, then return null.

You can assume that there are no spaces at the ends of the string and
that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy
dog" and k = 10, you should return:
["the quick",
 "brown fox",
 "jumps over",
 "the lazy",
 "dog"].

 No string in the list has a length of more than 10.
"""


def str_length_break(some_str=None, k=0):
    """Given a string, break it up so that at most each line is k-length."""
    if some_str is None or k == 0:
        return None
    one_line = ''
    result = []
    for one_word in some_str.split():
        if len(one_word) > k:
            return None
        one_line += ' ' + one_word
        if len(one_line) > k:
            len_last_word = len(one_word) + 1
            result.append(one_line[:-len_last_word])
            one_line = one_word
    else:
        result.append(one_line)
    return result


print(str_length_break("the quick brown fox jumps over the lazy dog", 10))
print(str_length_break("the quick brown fox jumps over the lazy dog", 4))
