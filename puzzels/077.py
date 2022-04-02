""" Prime summations

    Problem 77
    It is possible to write ten as the sum of primes in exactly five different ways:

        7 + 3
        5 + 5
        5 + 3 + 2
        3 + 3 + 2 + 2
        2 + 2 + 2 + 2 + 2

    What is the first value which can be written as the sum of primes in over five thousand different ways?
"""

from time import perf_counter
start = perf_counter()

# solution for problem 031
from lib.library import times_to_make_a_number, get_list_of_primes


def prime_summations(minimal_ways: int) -> None:
    primes = get_list_of_primes(minimal_ways)
    number, ways = 1, 0
    while ways <= minimal_ways:
        number += 1
        ways = times_to_make_a_number(primes, number)
    print(ways, number)


def main():

    prime_summations(5000)

    end = perf_counter()
    print(f"Runtime of the program is {end - start:.10f}")


if __name__ == "__main__":
    main()

# 5007 71
# Runtime of the program is 0.0237453000
