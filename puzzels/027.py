""" Quadratic primes

    Problem 27
    Euler discovered the remarkable quadratic formula:

        n^2 + n + 41

    It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
    However, when n = 40, 40^2 + 40 + 41 = 40(40+1) + 41 is divisible by 41, and certainly when
    n= 41, 41^2 + 41 + 41 is clearly divisible by 41.

    The incredible formula n^2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
    The product of the coefficients, −79 and 1601, is −126479.

    Considering quadratics of the form:

        n^2 + an + b, where |a| < 1000 and |b| ≤ 1000

        where |n| is the modulus/absolute value of n
        e.g. |11| = 11 and |−4| = 4

    Find the product of the coefficients, a and b, for the quadratic expression that produces the
    maximum number of primes for consecutive values of n, starting with n = 0.
"""

from time import perf_counter
start = perf_counter()

from lib.library import is_prime, get_list_of_primes


def consecutive_primes(a: int, b: int, i: int, prime: bool = True) -> int:
    if not prime:
        return i - 1
    return consecutive_primes(a, b, i + 1, is_prime((i + 1) ** 2 + a * (i + 1) + b))


def get_coef_for_longest_quadratic_primes_sequence(n: int) -> None:
    max_p, max_coef = 0, [0, 0]
    for a in range(-n + 1, n + 1, 2):
        for b in get_list_of_primes(n):
            consecutive = consecutive_primes(a, b, 0, True)
            if consecutive > max_p:
                max_p, max_coef = consecutive, [a, b]
    print(max_coef, max_p, max_coef[0] * max_coef[1])


get_coef_for_longest_quadratic_primes_sequence(1000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# [-61, 971] 74 -59231
# Runtime of the program is 0.4066479000
