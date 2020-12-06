from part1 import sum_counts_one, sum_counts_all

example_data = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def test_example_one():
    assert sum_counts_one(example_data) == 11

def test_example_all():
    assert sum_counts_all(example_data) == 6
