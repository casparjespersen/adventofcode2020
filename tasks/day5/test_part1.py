import pytest
from part1 import decode_row


@pytest.mark.parametrize("test_input,expected", [
    ("FBFBBFFRLR", (44, 5, 357)),
    ("BFFFBBFRRR", (70, 7, 567)),
    ("FFFBBBFRRR", (14, 7, 119)),
    ("BBFFBBFRLL", (102, 4, 820)),
])
def test_decoding(test_input: str, expected: tuple):
    assert decode_row(test_input) == expected
