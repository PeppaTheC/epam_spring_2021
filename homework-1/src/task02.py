"""
Given a cell with "it's a fib sequence" from the slideshow,
    please write a function "check_fib", which accepts a Sequence of integers, and
    returns whether the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contains >= 0 integers inside.
"""
from typing import Sequence


def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) < 3:
        return False

    if tuple(data[:3]) != (1, 1, 2):
        return False

    for i in range(len(data) - 2):
        if data[i] + data[i + 1] != data[i + 2]:
            return False

    return True
