""" Circular primes

    Problem 35
    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719,
    are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?
"""

# get a timer in place
from time import perf_counter

start = perf_counter()

# solution for problem 007
from lib.library import get_list_of_primes


def int_contains_digits(number: int, digits: list) -> bool:
    for digit in digits:
        if digit in str(number):
            return True
    return False


def is_circular_primes(prime: str, primes_list: list) -> bool:
    for i in range(1, len(prime)):
        if int(prime[i:] + prime[:i]) not in primes_list:
            return False
    return True


def circular_primes(n_bound: int) -> None:
    primes = get_list_of_primes(n_bound)

    # remove all the numbers containing 0, 2, 4, 5, 6, 8 (these cannot be prime)
    primes = [2] + [5] + [x for x in list(primes) if not int_contains_digits(x, ['0', '2', '4', '6', '8', '5'])]

    values = [[p for p in primes if 1 * 10 ** i >= p > 1 * 10 ** (i - 1)] for i in range(1, 7)]
    primes_by_digit_length = dict(zip(list(range(1, 7)), values))

    solution = {}
    for digit_length in range(1, 7):
        for prime in primes_by_digit_length[digit_length]:
            if is_circular_primes(str(prime), primes_by_digit_length[digit_length]):
                for index in range(len(str(prime))):
                    solution[str(prime)[index:] + str(prime)[:index]] = 1
    print(len(solution))


circular_primes(1000000)

end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")

# 55
# Runtime of the program is 0.0780503000
