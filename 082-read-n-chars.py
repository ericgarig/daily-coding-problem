u"""
Daily Coding Problem - 2018-12-29.

Using a read7() method that returns 7 characters from a file, implement
readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7()
returns “Hello w”, “orld” and then “”.

"""


def read7():
    """Read the first 7 characters."""
    global str_buffer
    result = str_buffer[:7]
    str_buffer = str_buffer[7:]
    print(result)
    return result


def read_n(n):
    """Read the first n characters."""
    global str_buffer
    result = str_buffer[:n]
    str_buffer = str_buffer[n:]
    print(result)
    return result


str_buffer = "Hello World"
read7()
read7()
read7()

str_buffer = "Hello World"
read_n(4)
read_n(4)
read_n(4)

str_buffer = "Hello World"
read_n(8)
read_n(8)
