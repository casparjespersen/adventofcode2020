from pathlib import Path
from copy import deepcopy
from part1 import input_file, _iterate_operations


def _iteration(operations: list):
    accumulator = 0
    index = 0
    visited = list()

    while True:
        if index >= len(operations):
            return accumulator, True
        if index in visited:
            return accumulator, False
        visited.append(index)
        operation, value = operations[index]
        if operation == "nop":
            index += 1
            continue
        if operation == "acc":
            accumulator += value
            index += 1
            continue
        if operation == "jmp":
            index += value
            continue

def _flip_operation(operation: str, value: int):
    if operation == "nop":
        return "jmp", value
    else:
        return "nop", value 

def find_fixed_accumulator(instructions: str):
    operations = list(_iterate_operations(instructions))
    pool = [i for i, (operation, _) in enumerate(operations) if operation in ("nop", "jmp")]

    for line in pool:
        mutated = deepcopy(operations)
        mutated[line] = _flip_operation(*mutated[line])
        accumulator, is_finite = _iteration(mutated)
        if is_finite:
            return accumulator


if __name__ == "__main__":
    accumulator = find_fixed_accumulator(input_file.read_text())
    print(f"{accumulator=}")
