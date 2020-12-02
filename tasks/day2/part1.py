""" Day 2: Password Philosophy

    Your flight departs in a few days from the coastal airport;
        the easiest way down to the coast from here is via toboggan.

    The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
    "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

    Their password database seems to be a little corrupted: some of the passwords wouldn't have
        been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

    To try to debug the problem, they have created a list (your puzzle input) of passwords
        (according to the corrupted database) and the corporate policy when that password was set.

    For example, suppose you have the following list:

    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc

    Each line gives the password policy and then the password.
    The password policy indicates the lowest and highest number of times a given letter must appear
        for the password to be valid. For example, 1-3 a means that the
            password must contain a at least 1 time and at most 3 times.

    In the above example, 2 passwords are valid.
        The middle password, cdefg, is not; it contains no instances of b, but needs at least 1.
        The first and third passwords are valid: they contain one a or ninz
            limits of their respective policies.

    How many passwords are valid according to their policies?
"""

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

        
