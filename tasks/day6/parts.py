from typing import Iterable, List
from pathlib import Path
from functools import reduce, partial

input_file = Path(__file__).parent / "input.txt"
input_text = input_file.read_text()


def _iterate_groups(input_data: str) -> Iterable[List[str]]:
    people = list()
    for line in input_data.split("\n"):
        if line == "":
            yield people
            people = list()
            continue
        people.append(set(line))
    if people:
        yield people


def _sum_counts(input_data: str, reducer: callable) -> int:
    all_yes = 0
    for group in _iterate_groups(input_data):
        group_yes = reduce(reducer, group)
        all_yes += len(group_yes)
    return all_yes

sum_counts_one = partial(_sum_counts, reducer=lambda x, y: x | y)
sum_counts_all = partial(_sum_counts, reducer=lambda x, y: x & y)

if __name__ == "__main__":
    print("part1", sum_counts_one(input_text))
    print("part2", sum_counts_all(input_text))
