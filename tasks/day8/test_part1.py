from part1 import find_preinfinite_accumulator

example = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

def test_example():
    assert find_preinfinite_accumulator(example) == 5
