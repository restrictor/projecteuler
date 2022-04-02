""" Convergents of e

    Problem 65
    ../images/065.png
"""

from time import perf_counter
start = perf_counter()

from fractions import Fraction
from sympy import E, N


# https://en.wikipedia.org/wiki/Periodic_continued_fraction#cite_note-7
# source Period of the Continued Fraction of √n by Marius Beceanu
def root_continued_fraction(s: float, ii: int) -> list:
    m0, d0, a0 = 0, 1, int(s)
    i, m, d, a, terms = 0, m0, d0, a0, [a0]
    while True:
        m = d * a - m
        d = (s ** 2 - m ** 2) / d
        a = int((s + m) / d)
        terms.append(a)
        i += 1
        if a == 2 * s or i == ii:
            break
    return terms


def continued_fraction_n(terms: list) -> Fraction:
    total = Fraction(1, terms[-1])
    for term in range(1, len(terms) - 1):
        total = Fraction(1, terms[len(terms) - term - 1] + total)
    return Fraction(terms[0], 1) + total


def get_sum_digits_numerator_100_continued_fraction_term_of_e(nth_term: int) -> None:
    e = N(E, 2*nth_term)
    terms = [int(fraction) for fraction in root_continued_fraction(e, nth_term-1)]
    print(nth_term, sum(map(int, str(continued_fraction_n(terms[:nth_term]).numerator))),
          continued_fraction_n(terms[:nth_term]))


get_sum_digits_numerator_100_continued_fraction_term_of_e(100)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 100 272 6963524437876961749120273824619538346438023188214475670667
# /2561737478789858711161539537921323010415623148113041714756 Runtime of the program is 0.5260247000
