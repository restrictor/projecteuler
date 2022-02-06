""" Truncatable primes

    Problem 37
    The number 3797 has an interesting property. Being prime itself, it is possible to
    continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7.
    Similarly we can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from time import perf_counter
start = perf_counter()

# for 2 digits length numbers the digits are both prime
# for 3 digits and higher the numbers 0,1,2,4,5,6,8 are not allowed in the middle
# 3/7   1/3/7/9     3/7                         for 3 digits
# 3/7   1/3/7/9     1/3/7/9     3/7             for 4 digits
# 3/7   1/3/7/9     1/3/7/9     1/3/7/9   3/7   for 4 digits
# etc

from itertools import product

# solution for problem 003
from lib.library import is_prime


def candidates_truncatable_primes(length: int) -> list:
    candidates = []

    candidates += ["".join(x) for x in product('12357', repeat=2)]

    for i in range(3, length):
        candidates += ["3" + "".join(x) + "3" for x in product('1379', repeat=i - 2)] \
                      + ["3" + "".join(x) + "7" for x in product('1379', repeat=i - 2)] \
                      + ["7" + "".join(x) + "3" for x in product('1379', repeat=i - 2)] \
                      + ["7" + "".join(x) + "7" for x in product('1379', repeat=i - 2)]
    return [y for y in [int(x) for x in candidates] if is_prime(y)]


def truncatable_primes(length: int) -> None:
    candidates_truncatable = candidates_truncatable_primes(length)
    sum_truncatable_primes, n_truncatable = 0, 0
    for prime in candidates_truncatable:
        string, truncatable = str(prime), True
        for y in [string[:i] for i in range(1, len(string))] + [string[i:] for i in range(1, len(string))]:
            if not is_prime(int(y)):
                truncatable = False
                break
        if truncatable:
            sum_truncatable_primes += prime
            n_truncatable += 1
            print(prime, n_truncatable)
    print(sum_truncatable_primes)


truncatable_primes(8)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 35 1
# 37 2
# 53 3
# 73 4
# 313 5
# 373 6
# 317 7
# 797 8
# 3137 9
# 3797 10
# 739397 11
# 748329
# Runtime of the program is 0.0979089000
