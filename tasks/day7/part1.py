import re
from pathlib import Path
from typing import Tuple
from collections import defaultdict
import numpy as np

input_file = Path(__file__).parent / "input.txt"
input_content = input_file.read_text()

pattern_line = re.compile(r"^([\w\s]+) bags contain ([\w\s,]+)\.$")
pattern_content = re.compile(r"^(\d+)\s([\w\s]+)\sbags?$")


def build_relationships(content: str) -> Tuple[list, np.ndarray]:
    """ Convert the textual input to a (total) list of bag types and a relationship matrix.
    """
    lines = content.split("\n")
    relations = defaultdict(dict)
    bag_types = set()

    # Interpret textual input
    for line in lines:
        if result := pattern_line.match(line):
            bag_type = result.group(1)
            bag_types.add(bag_type)
            content = result.group(2)
            for item in content.split(", "):
                if inner_result := pattern_content.match(item):
                    element_num = int(inner_result.group(1))
                    element_name = inner_result.group(2)
                    relations[bag_type][element_name] = element_num
                    bag_types.add(element_name)

    # Build relationship matrix
    bag_types = list(sorted(bag_types))
    matrix = np.zeros((len(bag_types), len(bag_types)), dtype=np.int)
    for i, bag_type in enumerate(bag_types):
        for (child_name, child_num) in relations[bag_type].items():
            matrix[i, bag_types.index(child_name)] = child_num

    return bag_types, matrix


def _recurse(matrix: np.ndarray, bag_index: int):
    container = set()
    parents = np.argwhere(matrix[:, bag_index] > 0)[:, 0]
    for index in parents:
        container.add(index)
        container = container | _recurse(matrix, index)
    return container


def derive_containing_types(content: str, bag_type: str = "shiny gold"):
    bag_types, matrix = build_relationships(content)
    bag_index = bag_types.index(bag_type)
    contained_within = _recurse(matrix, bag_index)
    return len(contained_within)


if __name__ == "__main__":
    print(derive_containing_types(input_content))