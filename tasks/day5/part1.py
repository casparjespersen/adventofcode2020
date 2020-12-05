from pathlib import Path


def decode_boarding_pass(value: str):
    assert len(value) == 10
    row = int(value[:7].replace("F", "0").replace("B", "1"), base=2)
    column = int(value[7:].replace("L", "0").replace("R", "1"), base=2)
    seat_id = row * 8 + column
    return row, column, seat_id


def fetch_boarding_passes():
    input_file = Path(__file__).parent / "input.txt"
    input_lines = input_file.read_text().split("\n")
    for item in input_lines:
        if item:
            yield item

if __name__ == "__main__":
    seat_ids = set()
    for boarding_pass in fetch_boarding_passes():
        _, _, seat_id = decode_boarding_pass(boarding_pass)
        seat_ids.add(seat_id)
    print(f"max: {max(seat_ids)}")
    