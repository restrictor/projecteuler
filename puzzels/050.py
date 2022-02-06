""" Consecutive prime sum

    Problem 50
    The prime 41, can be written as the sum of six consecutive primes:

        41 = 2 + 3 + 5 + 7 + 11 + 13
    This is the longest sum of consecutive primes that adds to a prime below one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a prime,
    contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

from time import perf_counter
start = perf_counter()

# solution for problem 003 and 007
from lib.library import get_list_of_primes, is_prime


def upper_bound_primes(upper_bound: int, primes_list: list) -> int:
    number_of_primes_upper_bound, upper = 21, 953
    while upper < upper_bound:
        upper = sum(primes_list[0:number_of_primes_upper_bound])
        number_of_primes_upper_bound += 1
    return number_of_primes_upper_bound


def get_longest_prime_is_consecutive_prime_sum(bound: int) -> None:
    primes = sorted(get_list_of_primes(bound))
    upper_bound = upper_bound_primes(bound, primes)
    found_solution, max_solution = False, []
    for length in range(upper_bound, 21, -1):
        for begin in range(0, upper_bound):
            if is_prime(sum(primes[begin:begin+length])) and sum(primes[begin:begin+length]) < bound:
                found_solution = True
                max_solution.append([sum(primes[begin:begin+length]), begin, length])
        if found_solution:
            print(max_solution)
            break


n_bound = 1000000
get_longest_prime_is_consecutive_prime_sum(n_bound)


end = perf_counter()
print(f"Runtime of the program is {end - start:.10f}")


# [[997651, 3, 543]]
# Runtime of the program is 0.0817005000