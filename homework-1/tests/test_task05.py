import pytest

from src.task05 import find_maximal_subarray_sum
from typing import List


@pytest.mark.parametrize(
    ["nums", "k", "expected_result"],
    [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, 16),
        ([-3, -5, -1, 0], 4, 0),
        ([1, -2, 0, 1], 4, 1)
    ],
)
def test_max_subarray_sum(nums: List[int], k: int, expected_result: bool):
    actual_result = find_maximal_subarray_sum(nums, k)

    assert actual_result == expected_result
