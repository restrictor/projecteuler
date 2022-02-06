from math import isqrt, gcd, sqrt
from typing import Iterator


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

