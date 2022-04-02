""" Ordered fractions

    Problem 71
    Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a
    reduced proper fraction.

    If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

        1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that 2/5 is the fraction immediately to the left of 3/7.

    By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size,
    find the numerator of the fraction immediately to the left of 3/7.
"""

from time import perf_counter
start = perf_counter()

# try a large value for denominator and reason if there can exist a different candidate


def get_largest_denominator_ordered_fraction(bound: int) -> None:
    numerator, denominator = 1, 1
    for i in range(bound, 1, -1):
        if i % 7 == 0:
            denominator = i
            numerator = denominator / 7 * 3
            break
    print(numerator - 1, denominator, (numerator - 1)/denominator, 3/7)


get_largest_denominator_ordered_fraction(1000000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 428570.0 999999 0.4285704285704286 0.42857142857142855
# Runtime of the program is 0.0000351000
