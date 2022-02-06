""" Non-abundant sums

    Problem 23
    A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
    For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means
    that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it is called
    abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
    as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers
    greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot
    be reduced any further by analysis even though it is known that the greatest number that cannot be expressed
    as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from time import perf_counter
start = perf_counter()

# solution for problem 021
from lib.library import proper_divisors


def is_abundant(n: int) -> bool:
    return sum(proper_divisors(n)) > n


def get_abundant(n: int) -> list:
    return [x for x in range(12, n) if is_abundant(x)]


def get_sum_of_not_a_abundant_sum(abu_d: dict) -> None:
    sum_of_not_a_abundant_sum = 1
    for i in range(2, 28123):
        not_a_sum_of_abundant = True
        for k in abu_d.values():
            if k < i:
                if i - k in abu_d:
                    not_a_sum_of_abundant = False
                    break
            else:
                break
        if not_a_sum_of_abundant:
            sum_of_not_a_abundant_sum += i
    print(sum_of_not_a_abundant_sum)


abundant_dict = {x: x for x in get_abundant(28123)}
get_sum_of_not_a_abundant_sum(abundant_dict)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 4179871
# Runtime of the program is 0.6614854000
