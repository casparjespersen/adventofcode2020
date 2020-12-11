from re import compile
from pathlib import Path

_pattern = compile(r"^(\w+)\s([\d+-]+)$")
input_file = (Path(__file__).parent / "input.txt")


def _iterate_operations(instructions: str):
    for line in instructions.split("\n"):
        result = _pattern.match(line)
        operation = result.group(1)
        value = int(result.group(2))
        yield operation, value


def find_preinfinite_accumulator(instructions: str):
    operations = list(_iterate_operations(instructions))
    accumulator = 0
    index = 0
    visited = list()

    while True:
        if index in visited:
            return accumulator
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


if __name__ == "__main__":
    accumulator = find_preinfinite_accumulator(input_file.read_text())
    print(f"{accumulator=}")
