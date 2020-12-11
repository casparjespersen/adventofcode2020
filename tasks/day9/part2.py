import numpy as np
from part1 import input_numbers, find_weaknesses


def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)


def find_encryption_weakness(numbers: list, target: int = 1398413738):
    _numbers = np.array(numbers)
    window_size = 2
    while True:
        print(f"Attempting with {window_size=}")
        for win in rolling_window(_numbers, window=window_size):
            if win.sum() == target:
                return win.min() + win.max()
        window_size += 1


if __name__ == "__main__":
    encryption_weakness = find_encryption_weakness(input_numbers)
    print(f"{encryption_weakness=}")
