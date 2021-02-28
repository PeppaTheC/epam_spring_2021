import pytest

from src.task03 import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["filename", "expected_result"],
    [
        ("test-file-1.txt", (1, 5)),    # [1,2,3,4,5]
        ("test-file-2.txt", (-1, 1)),   # [1,-1,0,1]
        ("test-file-3.txt", (0, 0)),    # [0,0,0]
    ],
)
def test_find_min_max(filename: str, expected_result: bool):
    actual_result = find_maximum_and_minimum(filename)

    assert actual_result == expected_result
