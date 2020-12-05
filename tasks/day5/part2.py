import numpy as np
from part1 import fetch_boarding_passes, decode_boarding_pass

if __name__ == "__main__":
    all_seats = list()
    for boarding_pass in fetch_boarding_passes():
        row, col, seat_id = decode_boarding_pass(boarding_pass)
        all_seats.append(seat_id)
    all_seats = np.array(sorted(all_seats))
    index = np.argwhere(np.diff(all_seats) == 2)[0][0]
    our_seat_id = all_seats[index] + 1
    print(f"{our_seat_id=}")
