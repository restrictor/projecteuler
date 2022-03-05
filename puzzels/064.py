""" Odd period square roots

    Problem 64
    ../images/064.png
"""

from time import perf_counter
start = perf_counter()

# solution for problem 046
from lib.library import is_perfect_square


# https://en.wikipedia.org/wiki/Periodic_continued_fraction#cite_note-7
# source Period of the Continued Fraction of √n by Marius Beceanu
def length_period_repeating_block(s: int) -> int:
    m0, d0, a0, result = 0, 1, int(s ** 0.5), 1
    m, d, a, aa = m0, d0, a0, [a0]
    while True:
        m = d * a - m
        d = (s - m ** 2) / d
        a = int((a0 + m) / d)
        result += 1
        if a == 2 * a0:
            break
    return result


def count_odd_length_period_repeating_block(bound: int) -> None:
    print(sum([length_period_repeating_block(i) % 2 == 0 for i in range(2, bound + 1) if not is_perfect_square(i)]))


count_odd_length_period_repeating_block(10000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 1322
# Runtime of the program is 0.1742176000
