""" Spiral primes

    Problem 58
    Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

        37 36 35 34 33 32 31
        38 17 16 15 14 13 30
        39 18  5  4  3 12 29
        40 19  6  1  2 11 28
        41 20  7  8  9 10 27
        42 21 22 23 24 25 26
        43 44 45 46 47 48 49

    It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting
    is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

    If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will
    be formed. If this process is continued, what is the side length of the square spiral for which the ratio
    of primes along both diagonals first falls below 10%?
"""

from time import perf_counter
start = perf_counter()

# to check faster primality test use Miller-Rabin: https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
from lib.library import get_list_of_primes


# implementation taken from: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
def try_composite(a: int, d: int, n: int, s: int) -> bool:
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2 ** i * d, n) == n - 1:
            return False
    return True


# implementation taken from: https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python
def is_prime_341_trillion(n: int, small_list: list) -> bool:
    if n in small_list:
        return True
    if any((n % p) == 0 for p in small_list) or n in (0, 1):
        return False
    if n >= 341550071728321:
        print(f"WARNING: the primality of {n} was not tested (number too large)")
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653:
        return not any(try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))


def spiral_primes_ration(ratio: float) -> None:
    p, i, primes = 0, 3, get_list_of_primes(20)
    while True:
        p += sum([is_prime_341_trillion(x, primes) for x in [i ** 2 - i + 1, i ** 2 - 2 * i + 2, i ** 2 - 3 * i + 3]])
        if p / float(2 * i + -1) < ratio:
            print(i)
            break
        i += 2


spiral_primes_ration(ratio=0.1)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 26241
# Runtime of the program is 0.2502690000
