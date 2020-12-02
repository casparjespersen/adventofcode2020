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

    