"""
Daily Coding Problem - 2018-11-04.

Write an algorithm to justify text. Given a sequence of words and an
integer line length k, return a list of strings which represents each
line, fully justified.

More specifically, you should have as many words as possible in each
line. There should be at least one space between each word. Pad extra
spaces when necessary so that each line has exactly length k. Spaces
should be distributed as equally as possible, with the extra spaces,
if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the
right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words:
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16, you should return the following:

[ "the  quick brown", # 1 extra space on the left
  "fox  jumps  over", # 2 extra spaces distributed evenly
  "the   lazy   dog"] # 4 extra spaces distributed evenly
"""


def pad_string(word_list, k):
    """Given a list of words and a str length, return a justified list."""
    result = []
    line_words = []
    len_words = 0
    for i in word_list:
        if (len_words + len(i) + len(line_words)) <= k:
            line_words.append(i)
            len_words += len(i)
        else:
            result.append(pad_one_line(line_words, k))
            line_words = [i]
            len_words = len(i)
    if line_words:
        result.append(pad_one_line(line_words, k))
    return result


def pad_one_line(word_list, k):
    """Given a list of words that fit on a line, justify them to length k."""
    if len(word_list) == 1:
        return word_list[0] + ' ' * (k - len(word_list[0]))
    spaces_to_add = k - len(''.join(word_list))
    max_space_per_word = ceildiv(spaces_to_add, len(word_list) - 1)
    result_str = word_list[0]
    for i in word_list[1:]:
        if max_space_per_word <= spaces_to_add:
            result_str += ' ' * max_space_per_word + i
            spaces_to_add -= max_space_per_word
        else:
            result_str += ' ' + i
    return result_str


def ceildiv(a, b):
    """Perform ceiling division."""
    return -(-a // b)


word_list = ["the", "quick", "brown",
             "fox", "jumps", "over",
             "the", "lazy", "dog"]
print(pad_string(word_list, 16))
