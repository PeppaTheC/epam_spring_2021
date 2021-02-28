import pytest

from src.task04 import check_sum_of_four
from typing import List


@pytest.mark.parametrize(
    ["a", "b", "c", "d", "expected_result"],
    [
        ([1, -1], [-1, 0], [0, 0], [0, 1], 4),
        ([1], [2], [-1], [-2], 1),
        ([0, 0], [0, 0], [0, 0], [0, 0], 16),
    ],
)
def test_check_sum(a: List[int], b: List[int], c: List[int], d: List[int], expected_result: bool):
    actual_result = check_sum_of_four(a, b, c, d)

    assert actual_result == expected_result
