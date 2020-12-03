from pathlib import Path
import numpy as np


def _load_map():
    input_file = Path(__file__).parent / "input.txt"
    input_lines = input_file.read_text().split("\n")
    matrix = list()
    for row in input_lines:
        vec = [True if char == "#" else False for char in row]
        matrix.append(vec)
    return np.array(matrix, dtype=np.bool)

x = _load_map()

def read_position(row: int, col: int) -> bool:
    global x
    if col >= x.shape[1]:
        # We reached the end of the row
        # Let us duplicate the map to the right
        print("Duplicating map")
        x = np.hstack((x, x))
    if row >= x.shape[0]:
        print("Reached the end..")
        raise StopIteration()
    return x[row, col]


def simulate_run(row_step: int, col_step: int):
    num_trees = 0
    row, col = 0, 0
    try:
        while True:
            num_trees += int(read_position(row, col))
            row += row_step
            col += col_step
    except StopIteration:
        return num_trees


if __name__ == "__main__":
    num_trees = simulate_run(1, 3)
    print(f"{num_trees=}")
