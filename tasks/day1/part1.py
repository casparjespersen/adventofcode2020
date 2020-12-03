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
