from itertools import combinations
from part1 import input_numbers
import numpy as np

if __name__ == "__main__":
    for numbers in combinations(input_numbers, r=3):
        if np.sum(numbers) == 2020:
            product = np.product(numbers)
            print(f"{numbers=} {product=}")
