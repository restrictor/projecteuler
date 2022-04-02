""" Coin sums

    Problem 31
    In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins
    in general circulation:

        1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

    It is possible to make £2 in the following way:

        1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?
"""

from time import perf_counter
start = perf_counter()


def times_to_make_a_number(values: list, total_sum: int) -> int:
    solution = [1] + [0] * total_sum
    for i in range(0, len(values)):

        # first we only update the solution[values[i]] for values[i]
        # next we add solution[j - values[i]] to solution[j]
        # so add the options to come with that coin to that value
        for j in range(values[i], total_sum + 1):
            solution[j] += solution[j - values[i]]
    return solution[total_sum]


coins_list = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
print(times_to_make_a_number(coins_list, amount))

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 73682
# Runtime of the program is 0.0002315000
