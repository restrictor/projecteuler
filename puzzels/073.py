""" Counting fractions in a range

    Problem 73
    Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called
    a reduced proper fraction.

    If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

        1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

    It can be seen that there are 3 fractions between 1/3 and 1/2.

    How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
"""

from time import perf_counter
start = perf_counter()

from itertools import compress


def sieve_coprimes(n: int) -> list:
    s = [True] * n
    for i in range(2, n):
        if n % i == 0 and s[i - 1]:
            s[i - 1::i] = [False] * len(s[i - 1::i])
            s[int(n / i) - 1::int(n / i)] = [False] * len(s[int(n / i) - 1::int(n / i)])
    return list(compress(list(range(1, n)), s))


def fraction_count(bound: int) -> None:
    total = 0
    for denominator in range(2, bound + 1):
        total += sum([1 for numerator in sieve_coprimes(denominator) if 1 / 2 > numerator / denominator > 1 / 3])
    print(total)


fraction_count(12000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 7295372
# Runtime of the program is 10.4365956000
