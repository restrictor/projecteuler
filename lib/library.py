from math import isqrt, gcd, sqrt
from typing import Iterator
from fractions import Fraction


# solution for problem 003
def is_prime(number: int) -> bool:
    if number < 2 or number % 2 == 0:
        return False
    elif number == 2:
        return True
    for num in range(3, int(number ** 0.5), 2):
        if number % num == 0:
            return False
    return True


# solution for problem 007
def get_list_of_primes(number: int) -> list:
    sieve = [True] * number
    for i in range(3, int(number ** 0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * ((number - i * i - 1) // (2 * i) + 1)
    primes = [2] + [i for i in range(3, number, 2) if sieve[i]]
    return primes


# solution for problem 021
def proper_divisors(n: int) -> Iterator[int]:
    yield 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            yield i
            if i < n / i:
                yield n / i


# solution for problem 034
def factorial(n: int) -> int:
    out = 1
    for i in range(1, n + 1):
        out *= i
    return out


# solution for problem 039
def pythagorean_triples(perimeter: int) -> list:
    triples = []
    for m in range(isqrt(perimeter - 1) + 1):
        for n in range(1 + m % 2, min(m, isqrt(perimeter - m * m) + 1), 2):
            if not gcd(m, n) > 1:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                for k in range(1, perimeter // c + 1):
                    triples += [(k * a, k * b, k * c)]
    return triples


# solution for problem 046
def is_perfect_square(n: int) -> bool:
    return int(sqrt(n) + 0.5) ** 2 == n


# solution for problem 047
def number_of_prime_factors(number: int) -> int:
    factors, i = set(), 2
    if number == 1:
        return 0
    while i < number ** 0.5:
        if number % i == 0:
            number = number / i
            factors.add(i)
            i -= 1
        i += 1
    return len(factors) + 1


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


# solution for problem 063
def is_perfect_n_cube(number: int, power: int) -> bool:
    return int(round(abs(number) ** (1. / power))) ** power == abs(number)


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


# solution for problem 065
def continued_fraction_n(terms: list) -> Fraction:
    total = Fraction(1, terms[-1])
    for term in range(1, len(terms) - 1):
        total = Fraction(1, terms[len(terms) - term - 1] + total)
    return Fraction(terms[0], 1) + total


# solution for problem 070
def totient_function(n: int) -> int:
    result = n
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            while n % i == 0:
                n = n / i
            result = result - result / i
    if n > 1:
        result = result - result / n
    return int(result)
