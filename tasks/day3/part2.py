from part1 import simulate_run

simulations = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1)
]

if __name__ == "__main__":
    trees_product = 1
    for (row_step, col_step) in simulations:
        trees_product *= simulate_run(row_step, col_step)
    print(f"{trees_product=}")
