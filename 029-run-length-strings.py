"""
Daily Coding Problem - 2018-11-05.

Run-length encoding is a fast and simple method of encoding strings. The
basic idea is to represent repeated successive characters as a single
count and character. For example, the string "AAAABBBCCDAA" would be
encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to
be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""


def encode_str(some_str=''):
    """Given a string, run-length encode it."""
    if not some_str:
        return None
    result = ''
    arr = list(some_str)
    current_char = arr.pop()
    run = 1
    while arr:
        last_char = arr.pop()
        if current_char != last_char or not arr:
            if not arr and current_char == last_char:
                run += 1
            result = str(run) + current_char + result
            current_char = last_char
            run = 0
        run += 1
    return result


print(encode_str('AAAABBBCCDAA'))    # 4A3B2C1D2A
print(encode_str('AABDDDDA'))    # 2A1B4D1A
print(encode_str(''))    # None
