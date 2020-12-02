import re
import numpy as np
from pathlib import Path

input_file = Path(__file__).parent / "input.txt"
input_lines = input_file.read_text().split("\n")
pattern = re.compile(r"(\d+)\-(\d+) (\w): (\w+)")

def decode_line(line: str) -> tuple:
    result = pattern.match(line)
    min_reps = int(result.group(1))
    max_reps = int(result.group(2))
    letter = result.group(3)
    password = result.group(4)
    return min_reps, max_reps, letter, password


def check_password_line(line: str) -> bool:
    min_reps, max_reps, letter, password = decode_line(line)
    num_characters_match = sum([1 for char in password if char == letter])
    return min_reps <= num_characters_match <= max_reps


if __name__ == "__main__":
    num_valid = sum(map(check_password_line, input_lines))
    print(f"{num_valid=}")

        
