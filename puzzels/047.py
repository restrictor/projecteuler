""" Distinct primes factors

    Problem 47
    The first two consecutive numbers to have two distinct prime factors are:

        14 = 2 × 7
        15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors are:

        644 = 2² × 7 × 23
        645 = 3 × 5 × 43
        646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime factors each.
    What is the first of these numbers?
"""

from time import perf_counter
start = perf_counter()


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


def first_4_consecutive_distinct_prime_factors(index: int) -> None:
    while True:
        if number_of_prime_factors(index) == 4:
            if number_of_prime_factors(index + 1) == 4:
                if number_of_prime_factors(index + 2) == 4:
                    if number_of_prime_factors(index + 3) == 4:
                        print(index)
                        break
        index += 3


first_4_consecutive_distinct_prime_factors(2*3*4*5)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 134043
# Runtime of the program is 0.9823109000
