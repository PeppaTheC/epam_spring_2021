import pytest

from src.task02 import check_fibonacci
from typing import Sequence


@pytest.mark.parametrize(
    ["data", "expected_result"],
    [
        ((1, 2, 3), False),
        ([1, 1, 2], True),
        (range(2), False),
        ((1, 1, 2), True),
        ((1, 1, 2, 3), True),
        ([1, 1], False),
        ((1, 1, 2, 3, 5, 7), False),
        ((), False),
    ],
)
def test_fibonacci(data: Sequence[int], expected_result: bool):
    actual_result = check_fibonacci(data)

    assert actual_result == expected_result
