""" Digit factorials

    Problem 34
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of their digits.

    Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from time import perf_counter
start = perf_counter()

import itertools as it


def factorial(n: int) -> int:
    out = 1
    for i in range(1, n + 1):
        out *= i
    return out


def upper_bound() -> int:
    i, fact_9 = 3, factorial(9)
    while i <= len(str(fact_9 * i)):
        i += 1
    return i - 1


def value_is_its_sum_digit_factorials(n_bound: int) -> None:
    sum_solutions = 0
    factorials = [factorial(i) for i in range(10)]

    candidates = []
    for n_digits in range(2, n_bound + 1):
        for x in it.combinations_with_replacement(range(10), n_digits):
            sum_digit_factorials = sum([factorials[x] for x in x])
            if sum_digit_factorials > 2:
                candidates.append(sum_digit_factorials)

    for candidate in set(candidates):
        if sum([factorials[int(digit)] for digit in str(candidate)]) == candidate:
            sum_solutions += candidate
            print(candidate)
    print(sum_solutions)


value_is_its_sum_digit_factorials(upper_bound())

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 145
# 40585
# 40730
# Runtime of the program is 0.0338680000
