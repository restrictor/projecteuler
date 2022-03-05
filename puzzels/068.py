""" Magic 5-gon ring

    Problem 68
    ../images/065.png
"""

from time import perf_counter
start = perf_counter()

# the number 10 should be in the outer region (outside) because 5 * 3 + 1 digits makes total 16 digits
# to maximize the concatenated digits, the numbers 1, 2, 3, 4, 5 should be in the inner region (inside)

import itertools


def test_config(configuration: list) -> bool:
    total_sum, k = configuration[0] + configuration[5] + configuration[6], 0
    for i in range(1, 5):
        if i == 4:
            k = 5
        if total_sum != configuration[0 + i] + configuration[5 + i] + configuration[6 + i - k]:
            return False
    return True


def solution(con: list) -> str:
    out_min, s = con.index(6), ''
    for i in range(5):
        s += str(con[(out_min + i) % 5]) + str(con[(out_min + 5 + i) % 5 + 5]) + str(con[(out_min + 6 + i) % 5 + 5])
    return s


def maximal_digital_magic_5_gon_ring() -> None:
    inside, outside, max_digits = [1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 0
    for outs in list(itertools.permutations(outside)):
        for ins in list(itertools.permutations(inside)):
            c = list(outs) + list(ins)
            if test_config(c):
                if max_digits < int(solution(c)):
                    max_digits = int(solution(c))
    print(max_digits)


maximal_digital_magic_5_gon_ring()

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# sol:  6531031914842725
# Runtime of the program is 0.0142916000
