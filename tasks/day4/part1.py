# missing cid is fine but missing any other field is not
# count number of valid passports

from pathlib import Path
from typing import Iterable, Dict


def read_batch(content: str):
    current = dict()

    for line in content.split("\n"):
        if len(line) == 0:
            yield current
            current = {}
            continue
        for part in line.split(" "):
            key, value = part.split(":")
            assert key not in current
            current[key] = value
    
    if current:
        yield current


def read_batch_input() -> Iterable[Dict[str, str]]:
    input_file = Path(__file__).parent / "input.txt"
    yield from read_batch(input_file.read_text())


if __name__ == "__main__":
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    num_valid = 0
    for item in read_batch_input():
        try:
            for field in required_fields:
                assert field in item
            num_valid += 1
        except AssertionError:
            continue
    print(f"{num_valid=}")
