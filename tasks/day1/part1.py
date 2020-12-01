""" Specifically, they need you to find the two entries that sum to 2020 and then multiply those two numbers together.

    For example, suppose your expense report contained the following:
        1721
        979
        366
        299
        675
        1456

    In this list, the two entries that sum to 2020 are 1721 and 299.
    Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

    Of course, your expense report is much larger.
    Find the two entries that sum to 2020; what do you get if you multiply them together?
"""

from pathlib import Path
from itertools import combinations
import numpy as np

input_file = Path(__file__).parent / "input.txt"
input_lines = input_file.read_text().split("\n")
input_numbers = np.array([int(x) for x in input_lines])

if __name__ == "__main__":
    for numbers in combinations(input_numbers, r=2):
        if np.sum(numbers) == 2020:
            product = np.prod(numbers)
            print(f"{numbers=} {product=}")
