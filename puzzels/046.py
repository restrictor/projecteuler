""" Goldbach's other conjecture

Problem 46
It was proposed by Christian Goldbach that every odd composite number can be written as the sum
of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from time import perf_counter
start = perf_counter()

import math

# solution for problem 007
from lib.library import get_list_of_primes


def is_perfect_square(n: int) -> bool:
    return int(math.sqrt(n) + 0.5) ** 2 == n


def first_odd_composite_number_breaks_conjecture(n_bound: int) -> None:

    # use primes and non primes to decide the cases
    primes = set(get_list_of_primes(n_bound))
    composites = set(range(3, n_bound, 2)) - primes

    for composite in composites:
        does_not_breaks_conjecture = False
        for prime in [p for p in primes if p < composite]:
            if is_perfect_square((composite - prime) / 2):
                does_not_breaks_conjecture = True
                break
        if not does_not_breaks_conjecture:
            print(composite)
            break


first_odd_composite_number_breaks_conjecture(6000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 5777
# Runtime of the program is 0.1346171000
