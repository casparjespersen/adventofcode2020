from pathlib import Path
from itertools import combinations
import numpy as np

input_file = Path(__file__).parent / "input.txt"
input_numbers = list(map(int, input_file.read_text().split("\n")))


def find_weaknesses(numbers: list, preamble: int):
    for i in np.arange(start=preamble, stop=len(numbers)):
        leading = numbers[(i-preamble):i]
        value = numbers[i]
        sum_pool = {np.sum(pair) for pair in combinations(leading, r=2)}
        if value not in sum_pool:
            yield value, leading


def find_weakness(numbers: list, preamble: int):
    for weakness, _ in find_weaknesses(numbers, preamble):
        return weakness


if __name__ == "__main__":
    first_weakness = find_weakness(input_numbers, preamble=25)
    print(f"{first_weakness=}")
