"""
Write down a function, which reads input line-by-line, and finds maximum and minimum values.
The function should return a tuple with the max and min values.
For example for [1, 2, 3, 4, 5], function should return [1, 5]
We guarantee, that file exists and contains line-delimited integers.
To read file line-by-line you can use this snippet:
with open("some_file.txt") as fi:
    for line in fi:
        ...
"""
from typing import Tuple


def find_maximum_and_minimum(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        nums = []
        for line in fi:
            nums.append(int(line))

    if len(nums) == 0:
        raise ValueError("No numbers have been found.")

    return min(nums), max(nums)
