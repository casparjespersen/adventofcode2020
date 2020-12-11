import re
from pathlib import Path
from typing import Tuple
from collections import defaultdict
import numpy as np
from part1 import build_relationships, input_content


def _recurse(matrix: np.ndarray, bag_index: int) -> int:
    bags = 0
    children = np.argwhere(matrix[bag_index, :] > 0)[:, 0]
    for index in children:
        bags += matrix[bag_index, index] * (1 + _recurse(matrix, index))
    return bags


def derive_contained_bags(content: str, bag_type: str = "shiny gold") -> int:
    bag_types, matrix = build_relationships(content)
    bag_index = bag_types.index(bag_type)
    num_contains = _recurse(matrix, bag_index)
    return num_contains


if __name__ == "__main__":
    print(derive_contained_bags(input_content))