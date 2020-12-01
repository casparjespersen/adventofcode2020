""" Using the above example again, the three entries that sum to 2020 are 979, 366, and 675.
        Multiplying them together produces the answer, 241861950.

    In your expense report, what is the product of the three entries that sum to 2020?
"""

from itertools import combinations
from part1 import input_numbers
import numpy as np

if __name__ == "__main__":
    for numbers in combinations(input_numbers, r=3):
        if np.sum(numbers) == 2020:
            product = np.product(numbers)
            print(f"{numbers=} {product=}")
