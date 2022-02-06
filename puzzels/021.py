""" Amicable numbers

    Problem 21
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are
     called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
    therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
"""

from time import perf_counter
start = perf_counter()
from typing import Iterator


def proper_divisors(n: int) -> Iterator[int]:
    yield 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            yield i
            if i < n / i:
                yield n / i


def sum_proper_divisors(n: int) -> int:
    return sum(proper_divisors(n))


def sum_amicable_numbers(n: int) -> None:
    sum_of_proper_of_n, ss = {}.fromkeys(set([i for i in range(10000)])), []
    for candidate in range(1, n):
        if not sum_of_proper_of_n[candidate]:
            a = sum_proper_divisors(candidate)
            b = sum_proper_divisors(a)
            if b == candidate:
                if a != b:
                    sum_of_proper_of_n[candidate], sum_of_proper_of_n[a] = a, candidate
                    ss.extend([candidate, a])
                else:
                    sum_of_proper_of_n[candidate] = 0
            else:
                sum_of_proper_of_n[candidate] = 0
    print(ss, sum(ss))


n_bound = 10000
sum_amicable_numbers(n_bound)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# [220, 284.0, 1184, 1210.0, 2620, 2924.0, 5020, 5564.0, 6232, 6368.0] 31626.0
# Runtime of the program is 0.0968154000
