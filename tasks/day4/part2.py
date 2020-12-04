import re
from pathlib import Path
from part1 import read_batch, read_batch_input


def verify_passport(item: dict):
    try:
        assert 1920 <= int(item["byr"]) <= 2002
        assert 2010 <= int(item["iyr"]) <= 2020
        assert 2020 <= int(item["eyr"]) <= 2030    
        assert item["ecl"] in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        assert re.match(r"^#[0-9a-f]{6}$", item["hcl"])
        assert re.match(r"^\d{9}$", item["pid"])
        height = re.match(r"^(\d+)(cm|in)$", item["hgt"])
        value = int(height.group(1))
        unit = height.group(2)
        assert unit in ("cm", "in")
        if unit == "cm":
            assert 150 <= value <= 193
        elif unit == "in":
            assert 59 <= value <= 76
        return True
    except:
        return False

# Test invalid passports
_invalid_passports = (Path(__file__).parent / "part2_invalid.txt").read_text()
for item in read_batch(_invalid_passports):
    assert not verify_passport(item)

# Test valid passports
_valid_passports = (Path(__file__).parent / "part2_valid.txt").read_text()
for item in read_batch(_valid_passports):
    assert verify_passport(item)

if __name__ == "__main__":
    num_valid = 0
    for item in read_batch_input():
        num_valid += int(verify_passport(item))
    print(f"{num_valid=}")
