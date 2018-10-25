"""
Daily Coding Problem - 2018-10-14.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

You can assume that the messages are decodable.
For example, '001' is not allowed.

E.g.: '111' would give 3 --> 'aaa', 'ka', 'ak'
      '121' would give 3 --> 'aba', 'au', 'la'
      '1234' would give 3 --> 'ABCD', 'LCD', 'AWD'
      '1221' would give 5 --> 'ABBA', 'ABU', 'AVA', 'LU', 'LBA'
"""


def count_decode(digit_list):
    """Given a number string, return how many ways it can be decoded."""
    if len(digit_list) == 0:
        return 1
    nums = 0
    if digit_list[0] != 0:
        nums += count_decode(digit_list[1:])
    double_digit_num = int(''.join(map(str, digit_list[0:2])))
    if double_digit_num > 9 and double_digit_num < 27:
        # only digits double-digit int upto 26 ( since there are 26 letters)
        nums += count_decode(digit_list[2:])
    return nums


count_decode([1, 1, 1])
count_decode([1, 2, 3, 4])
count_decode([1, 2, 2, 1])
