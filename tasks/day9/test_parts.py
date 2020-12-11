from part1 import find_weakness
from part2 import find_encryption_weakness

example = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

numbers = list(map(int, example.split("\n")))

def test_example():
    assert find_weakness(numbers, preamble=5) == 127

def test_part2():
    assert find_encryption_weakness(numbers, target=127) == 62
