""" Square root digital expansion

    Problem 80
    It is well known that if the square root of a natural number is not an integer, then it is irrational.
    The decimal expansion of such square roots is infinite without any repeating pattern at all.

    The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal
    digits is 475.

    For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal
    digits for all the irrational square roots.
"""

from time import perf_counter
start = perf_counter()

from decimal import Decimal as Dec, getcontext
from math import floor, sqrt

# solution for problem 065
from lib.library import continued_fraction_n as cont_frac_n


# modification on:
# https://en.wikipedia.org/wiki/Periodic_continued_fraction#cite_note-7
# source Period of the Continued Fraction of √n by Marius Beceanu
def continued_fraction(s: int) -> list:
    m0, d0, a0 = 0, 1, int(sqrt(s))
    i, m, d, a, aa = 0, m0, d0, a0, [a0]
    while True:
        m = d * a - m
        d = (s - m ** 2) / d
        a = floor((a0 + m) / d)
        aa.append(a)
        i += 1
        if a == 2 * a0:
            break
    return aa


def get_total_digital_sum_decimal_digits(n_digits: int, bound: int, precision: int) -> None:
    total = 0
    for i in range(1, bound + 1):
        if i != (int(sqrt(i)) ** 2):
            cont_frac = [int(x) for x in continued_fraction(i)]
            cont_frac = cont_frac + cont_frac[1:] * precision

            numerator = cont_frac_n(cont_frac[:precision]).numerator
            denominator = cont_frac_n(cont_frac[:precision]).denominator
            digits = str(Dec(numerator) / Dec(denominator))[0:n_digits+1]
            total += sum([int(digit) for digit in digits if digit != '.'])
    print(total)


def main():

    precision = 200
    getcontext().prec = precision

    get_total_digital_sum_decimal_digits(100, 100, precision)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# 40886
# Runtime of the program is 0.2054487000
