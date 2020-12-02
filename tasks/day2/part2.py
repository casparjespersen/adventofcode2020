"""
--- Part Two ---

While it appears you validated the passwords correctly,
    they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules
    from his old job at the sled rental place down the street!
    The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where
    1 means the first character,
    2 means the second character, and so on.
    (Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
    Exactly one of these positions must contain the given letter.
    Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

    1-3 a: abcde is valid: position 1 contains a and position 3 does not.
    1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
    2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.

How many passwords are valid according to the new interpretation of the policies?
"""

from part1 import decode_line, input_lines


def check_password_line(line: str):
    index_0, index_1, letter, password = decode_line(line)
    num_match = 0
    num_match += int(password[index_0 - 1] == letter)
    num_match += int(password[index_1 - 1] == letter)
    return num_match == 1


if __name__ == "__main__":
    num_valid = sum(map(check_password_line, input_lines))
    print(f"{num_valid=}")

    